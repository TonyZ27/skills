# Skills Catalog Instructions

This directory is organized by how skills are used. When adding, moving, or relocating a skill, place it in the matching category folder below.

## Canonical Categories

- `01-planning/`
  - Use for brainstorming, planning, PRDs, specs, and multi-step execution-planning skills.
- `02-design-and-frontend/`
  - Use for UI, UX, frontend, animation, accessibility, React, and visual design skills.
- `03-figma/`
  - Use for Figma workflows, plugins, design systems, tokens, variables, and design-to-code skills.
- `04-skill-management/`
  - Use for creating, evaluating, benchmarking, finding, installing, or improving skills.
- `05-docs-and-recaps/`
  - Use for README generation, documentation helpers, recaps, retrospectives, and summary-oriented skills.

## Placement Rules

- A canonical skill should live exactly one level below its category folder.
  - Example: `03-figma/my-figma-skill/SKILL.md`
- Keep one canonical copy of each skill in the numbered folders.
- Do not leave canonical skills at the repository root.

## Non-Canonical Content

- `_workspaces/`
  - Use for skill workspaces, iteration outputs, eval runs, snapshots, and experiment artifacts.
  - Directories ending in `-workspace` belong here.
- `_archive/`
  - Use for duplicates, deprecated copies, and anything that should not be treated as a primary skill.

## Relocation Guidance

- If a new skill clearly fits one category, move it there directly.
- If a skill could fit multiple categories, choose based on its primary trigger and main job, not secondary features.
- If the correct category is unclear, ask before moving it.
- Do not reorganize existing skills unless the user asked for relocation.
- Do not delete workspace or archive material unless the user asked for cleanup.
