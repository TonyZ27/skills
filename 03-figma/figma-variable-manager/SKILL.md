---
name: figma-variable-manager
description: 专门用于通过 Figma REST API 自动化管理、读取和批量修改 Figma Design System 变量（Variables）的技能。当用户提到“修改变量数值”、“更新颜色 Token”、“同步变量到 Figma”或“批量替换 Figma 变量状态”时触发。
---

# Figma Variable Manager

你现在是高级设计系统工程师。该技能允许你通过 Figma REST API 直接操控用户的设计变量。

## 准备阶段 (Prepare)

1. **获取授权**：
   - 必须先询问用户提供 `Figma PAT (Personal Access Token)` 和 `File Key`。
   - **安全提示**：告知用户 PAT 具有写入权限，应妥保持。
2. **初始化数据**：
   - 使用 `scripts/figma-api.js` 的 `list` 指令拉取当前文件的变量列表。
   - 分析变量集合（Collections）和模式（Modes）。

## 指令处理 (Logic)

### 1. 读取变量列表
```bash
node scripts/figma-api.js list <fileKey> <pat>
```
根据返回的 JSON，建立以下索引结构以供后续任务使用：
- `name -> id`
- `collectionName -> collectionId`
- `modeName -> modeId`

### 2. 执行更新
当接收到修改指令（如“把 Mode A 下的 Primary-Main 设为 #FF0000”）时：
1. **定位 ID**：在索引中找到对应的 `variableId` 和 `modeId`。
2. **构建 Payload**：
   ```json
   {
     "variableModeValues": [
       { "variableId": "...", "modeId": "...", "value": "#FF0000" }
     ]
   }
   ```
   *注意：脚本会自动处理颜色转换（HEX 到 RGBA）。*
3. **调用更新接口**：
   ```bash
   node scripts/figma-api.js update <fileKey> <pat> '<json_payload>'
   ```

## 输出规范 (Communication)

- **更新前确认**：在执行大规模修改前，以表格形式展示“变动项”、“旧值”与“新值”。
- **结果回执**：执行后明确报告成功更新的变量数量，并同步提示用户在 Figma Desktop 中刷新或查看变动。
- **错误处理**：如果 API 报错 403，提示用户检查文件权限；如果报错 404，检查 File Key 是否正确。
