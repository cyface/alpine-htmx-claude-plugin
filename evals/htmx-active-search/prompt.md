---
description: htmx skill should produce a debounced, de-duplicated active search with an indicator
tags: [htmx]
max_turns: 15
allowed_tools: [Read, Glob, Grep, Skill]
---

I have a Django app with a /customers/search/ view that returns a rendered <table> of matching rows for a ?q= parameter. Add search-as-you-type to this input with htmx so results appear below it without a page reload. It should not hammer the server while people type, stale responses must not overwrite newer ones, and users should see that a search is in progress.

<input type="search" name="q" placeholder="Search customers">
<div id="results"></div>
