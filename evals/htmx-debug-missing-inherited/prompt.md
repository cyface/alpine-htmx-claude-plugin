---
description: htmx-debug should spot that htmx 4 needs :inherited and the 2.x event name never fires
tags: [htmx, debug]
max_turns: 15
allowed_tools: [Read, Glob, Grep, Skill]
---

We just bumped our script tag from htmx.org@2.0.10 to htmx.org@4.0.0 and the admin page broke. Clicking the buttons makes a request (I can see it in the network tab, 200 OK, HTML body) but the table never updates, and the little "Updated!" toast we trigger from JS stopped appearing. Nothing in the console. Here's the relevant markup:

<div hx-target="#orders-table" hx-swap="innerHTML" hx-headers='{"X-CSRFToken": "abc123"}'>
  <button hx-get="/orders?status=open">Open</button>
  <button hx-get="/orders?status=closed">Closed</button>
</div>
<table id="orders-table">...</table>

<script>
document.body.addEventListener('htmx:afterSwap', function () { showToast('Updated!') })
</script>

What's going on?
