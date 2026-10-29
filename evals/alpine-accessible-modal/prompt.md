---
description: Alpine skill should produce an accessible modal (dialog role, focus trap, escape, focus return)
tags: [alpine]
max_turns: 15
allowed_tools: [Read, Glob, Grep, Skill]
---

I'm using Alpine.js with Tailwind on a plain server-rendered site (no build step, Alpine from a CDN). Write me a reusable "Delete account" confirmation modal: a button opens it, it has a title and Cancel / Delete buttons, clicking the backdrop or pressing Escape closes it. Make it properly accessible for screen reader and keyboard users. Just give me the HTML snippet plus whatever script tags I need in the head.
