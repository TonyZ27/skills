#!/usr/bin/env node

/**
 * Figma Variables REST API Client
 * Usage: node figma-api.js <action> <fileKey> <pat> [payload]
 */

const https = require('https');

const args = process.argv.slice(2);
const [action, fileKey, pat, payloadStr] = args;

if (!action || !fileKey || !pat) {
    console.error('Usage: node figma-api.js <list|update> <fileKey> <pat> [payload]');
    process.exit(1);
}

const headers = {
    'X-Figma-Token': pat,
    'Content-Type': 'application/json'
};

/**
 * Helper to make HTTPS requests
 */
function request(method, path, body = null) {
    return new Promise((resolve, reject) => {
        const options = {
            hostname: 'api.figma.com',
            path,
            method,
            headers
        };

        const req = https.request(options, (res) => {
            let data = '';
            res.on('data', (chunk) => data += chunk);
            res.on('end', () => {
                if (res.statusCode >= 200 && res.statusCode < 300) {
                    resolve(JSON.parse(data));
                } else {
                    reject(new Error(`API Error ${res.statusCode}: ${data}`));
                }
            });
        });

        req.on('error', reject);
        if (body) req.write(JSON.stringify(body));
        req.end();
    });
}

/**
 * HEX to RGBA (for Figma API)
 */
function hexToRgba(hex) {
    hex = hex.replace('#', '');
    if (hex.length === 3) hex = hex.split('').map(c => c + c).join('');
    const r = parseInt(hex.substring(0, 2), 16) / 255;
    const g = parseInt(hex.substring(2, 4), 16) / 255;
    const b = parseInt(hex.substring(4, 6), 16) / 255;
    return { r, g, b, a: 1 };
}

async function run() {
    try {
        if (action === 'list') {
            const data = await request('GET', `/v1/files/${fileKey}/variables/local`);
            console.log(JSON.stringify(data, null, 2));
        } else if (action === 'update') {
            const payload = JSON.parse(payloadStr);
            // payload example: { "variableModeValues": [{ "variableId": "...", "modeId": "...", "value": ... }] }
            // Transform HEX strings to RGBA objects automatically if they look like colors
            if (payload.variableModeValues) {
                payload.variableModeValues = payload.variableModeValues.map(item => {
                    if (typeof item.value === 'string' && /^#([A-Fa-f0-9]{3}){1,2}$/.test(item.value)) {
                        item.value = hexToRgba(item.value);
                    }
                    return item;
                });
            }
            const res = await request('POST', `/v1/files/${fileKey}/variables`, payload);
            console.log(JSON.stringify({ status: 'success', data: res }, null, 2));
        }
    } catch (err) {
        console.error(JSON.stringify({ status: 'error', message: err.message }, null, 2));
        process.exit(1);
    }
}

run();
