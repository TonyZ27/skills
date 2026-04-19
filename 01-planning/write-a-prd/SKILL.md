---
name: write-a-prd
description: Create dual PRDs (Technical and Design) through user interview, codebase exploration, user flow analysis, and module design. Use when user wants to write a PRD, create product requirements documents, or plan a new feature covering both design and engineering scopes.
---

This skill will be invoked when the user wants to create product requirements documents (PRDs). You will generate TWO separate documents: a Design PRD and a Technical PRD. You may skip steps if you don't consider them necessary.

1. Ask the user for a long, detailed description of the problem they want to solve, the target audience, user experience goals, and any potential technical solutions.

2. Explore the codebase (if applicable) to verify their assertions and understand the current technical implementation and UI state.

3. Interview the user relentlessly about both the Interaction/UX layer and the Technical Implementation layer until you reach a shared understanding. Walk down each branch of the design tree:
   - For Design/UX: Clarify user flows, page hierarchies, edge cases (empty states, error handling, loading screens), and general visual/interaction constraints.
   - For Technical: Clarify architecture, deep modules, schema changes, database models, testing strategies, and API contracts.

4. Sketch out the major workflows and technical modules needed. 
   - A deep technical module encapsulates a lot of functionality in a simple, testable interface.
   - A robust UX flow covers all interaction states seamlessly without dead ends.
   Check with the user that these structures match their expectations before writing.

5. Once you have a complete understanding, generate TWO separate, exhaustive PRDs using the templates below. Output them clearly separated in your response or submit them as two distinct GitHub issues/files, as preferred by the user.

<design-prd-template>
## Problem Statement
The problem that the user is facing, from the user's perspective.

## Solution & Value Proposition
The solution to the problem and the core value it provides, from the user's perspective.

## User Stories
A LONG, numbered list of user stories covering all aspects of the feature. Each in the format:
1. As an <actor>, I want a <feature>, so that <benefit>

## Interaction Framework & Information Architecture
A detailed breakdown of the user flow, page hierarchy, and how users navigate through the feature. Include logical paths and entry/exit points.

## UI/UX Edge Cases
A comprehensive list defining how the interface behaves in out-of-bound scenarios:
- Loading states
- Empty states
- Error handling & validation failing
- Network failures

## Accessibility & Visual Constraints
Specific visual paradigms, responsive design requirements, and accessibility notes (e.g., keyboard navigation).
</design-prd-template>

<technical-prd-template>
## Architecture & Deep Modules
A list of the deep modules that will be built or modified, highlighting high cohesion and low coupling.

## Implementation Decisions
Specific technical implementation decisions, including:
- The interfaces of those modules that will be modified
- Technical clarifications from the developer
- Schema & Data Model changes
- API contracts and data flows

Do NOT include specific file paths or code snippets. They may end up being outdated very quickly.

## Testing Decisions
A list of testing decisions that were made. Include:
- A description of what makes a good test (only test external behavior)
- Which modules will be unit-tested vs. end-to-end tested
- Prior art for the tests

## Out of Scope
A description of the things that are out of scope for this task (both frontend and backend).

## Further Notes
Any further technical notes.
</technical-prd-template>
