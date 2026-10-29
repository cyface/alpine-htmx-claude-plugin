---
description: htmx-upgrade should convert a 2.x template to 4 with the right renames, inheritance, and event names
tags: [htmx, upgrade]
max_turns: 20
allowed_tools: [Read, Glob, Grep, Skill]
---

We're moving our Flask app to htmx 4. Please convert this Jinja template and the inline script, and tell me anything I need to change on the server side.

<body hx-headers='{"X-CSRFToken": "{{ csrf_token() }}"}' hx-boost="true">
  <form hx-post="/items" hx-target="#items" hx-swap="beforeend" hx-disabled-elt="find button">
    <input name="name" required>
    <button>Add</button>
  </form>
  <ul id="items">
    {% for item in items %}
    <li id="item-{{ item.id }}">
      {{ item.name }}
      <button hx-delete="/items/{{ item.id }}" hx-target="closest li" hx-swap="outerHTML" hx-confirm="Delete?">x</button>
    </li>
    {% endfor %}
  </ul>
  <div hx-get="/jobs/status" hx-trigger="every 3s" hx-swap="innerHTML">pending</div>
  <div hx-disable>
    <div id="map"></div>
  </div>
  <script>
    document.body.addEventListener('htmx:configRequest', function (e) {
      e.detail.headers['X-Timezone'] = Intl.DateTimeFormat().resolvedOptions().timeZone
    })
    document.body.addEventListener('htmx:responseError', function (e) {
      alert('Request failed: ' + e.detail.xhr.status)
    })
  </script>
</body>
