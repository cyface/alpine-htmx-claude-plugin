---
description: Combined Alpine + htmx usage must keep Alpine state outside the swap target and use kebab-case htmx events
tags: [alpine, htmx, integration]
max_turns: 20
allowed_tools: [Read, Glob, Grep, Skill]
---

I'm building an admin page with Alpine.js and htmx (Flask backend, Jinja templates). I need an "Edit note" flow: a button opens an Alpine modal containing a form; submitting the form posts to /notes/<id> with htmx, which responds with the updated note's <li> that should replace the matching item in the list below. On success the modal should close; on a validation error (422 with the re-rendered form) the form should stay open showing the errors. Please write the HTML.

<ul id="notes">
  <li id="note-42">Buy milk <button>Edit</button></li>
</ul>
