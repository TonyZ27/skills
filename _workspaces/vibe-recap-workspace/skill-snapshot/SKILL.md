---
name: vibe-recap
description: Recap a vibe coding session by reading conversation history, extracting decisions, mistakes, pivots, and collaboration patterns, then turning them into a useful retrospective with actionable next-step advice. Use this whenever the user asks to recap, review, reflect on, summarize lessons from, or extract patterns from a coding conversation, development session, debugging thread, or AI pair-programming workflow, even if they do not explicitly say "retrospective" or "postmortem."
---

# Vibe Recap

Use this skill to turn a messy or intuitive coding session into a clear retrospective. The goal is not to merely summarize what happened. The goal is to help the user understand how they worked, where momentum was gained or lost, which patterns are worth repeating, and what should change next time.

## What This Skill Produces

Produce a coaching-style recap that does four things:

1. Reconstruct the arc of the session
2. Surface meaningful working patterns, not just events
3. Explain why certain moments helped or hurt progress
4. End with concrete advice the user can apply in the next session

Keep the tone sharp, supportive, and grounded in evidence from the source material.

## When To Use It

Use this skill when the user wants any of the following:

- A recap of a coding session
- A retrospective on a vibe coding workflow
- Lessons learned from a conversation history
- A summary of what went well, what got messy, and how to improve
- Pattern extraction from an AI-assisted dev session
- A postmortem-style reflection on a build, bugfix, prototype, or exploration

This skill is a good fit even when the user phrases the request loosely, such as:

- "help me make sense of this session"
- "what can I learn from this thread"
- "summarize how I worked here"
- "pull out the patterns from this convo"
- "review my vibe coding process"

Do not use this skill when the user only wants a plain chronological summary with no reflection. In that case, provide a normal summary unless the user asks for lessons, patterns, or advice.

## Inputs

Prefer these sources in order:

1. The current conversation or thread, if it contains the relevant working session
2. A user-provided transcript, markdown export, or pasted conversation history
3. Supporting artifacts the user explicitly points to, such as plans, TODO notes, commit messages, or scratch docs

If multiple sources exist, combine them carefully and say which ones you used.

## Source Handling

Before writing the recap:

1. Identify the session goal or goals
2. Reconstruct the major phases of the session
3. Note turning points:
   - requirement changes
   - debugging breakthroughs
   - dead ends
   - ambiguous instructions
   - moments where the user corrected the approach
4. Track how decisions were made:
   - by intuition
   - by trial and error
   - by explicit planning
   - by reading code or docs
5. Separate signal from noise

Do not overweight sheer repetition. A repeated issue matters only if it reveals a pattern.

## Analysis Lens

Look for patterns like these:

- Strong prompts or framing that unlocked progress
- Weak prompts that created drift or needless work
- Places where requirements were clarified too late
- Times when the session moved too fast without verification
- Good instincts the user should keep using
- Recurring friction in collaboration, debugging, or scope control
- Evidence that the user needed a checklist, template, or reusable workflow

Focus on behaviors and decision quality, not blame.

## Output Rules

Default to a structured recap. Read the template in `references/output-template.md` and follow it unless the user asks for a different format.

Ground every major conclusion in evidence from the conversation. Do not invent root causes that are not supported by the source. If something is an inference, label it as an inference.

Keep the recap compact but insightful:

- short session: 5-8 paragraphs or equivalent sections
- long session: concise sections with bullets where useful

Avoid transcript-style blow-by-blow narration unless the user explicitly asks for it.

## Writing Guidance

Write like a thoughtful coach who actually paid attention.

- Be specific
- Use the user's real workflow details
- Point out what was effective, not only what failed
- Turn vague advice into repeatable moves

Good: "You moved faster once the task shifted from 'fix everything in one pass' to 'confirm the output contract first and then patch the bug.' That suggests your future sessions benefit from locking the acceptance shape before implementation."

Weak: "Planning more could help."

## Adaptation Modes

If the user asks for a specific style, adapt:

- `quick recap`: compress to summary + lessons + next steps
- `deep retrospective`: spend more space on patterns, causes, and repeated behaviors
- `team share-out`: make it more readable for others and less introspective
- `personal coaching`: lean harder into habits, prompts, and working style suggestions

If no style is specified, use `personal coaching`.

## Failure Modes To Avoid

Do not:

- merely restate the transcript
- overpraise without insight
- turn one-off events into sweeping claims
- give generic advice that could apply to any session
- ignore the user's stated goal for the session

## Example Requests

Example 1:
Input: "Read this conversation history and recap my vibe coding session. I want to know what patterns I should keep and what kept slowing me down."
Output: A coaching-style retrospective with session arc, helpful patterns, friction points, lessons, and next-session advice.

Example 2:
Input: "Can you review this AI coding thread and turn it into a short postmortem for me?"
Output: A concise retrospective with what happened, what changed, what was learned, and concrete follow-ups.
