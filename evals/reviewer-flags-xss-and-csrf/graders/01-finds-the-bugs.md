---
type: llm
---

PASS if the review identifies ALL of the following:
- x-html on user-authored comment bodies is a stored XSS risk, and recommends x-text (or server-side sanitisation / server rendering) instead.
- The Alpine listener @htmx:afterRequest is camelCase and will never fire; it must be @htmx:after-request on htmx 2.x or @htmx:after:request on htmx 4 (mentioning either correct form, or both, is fine).
- The x-for loop lacks a :key binding, OR the review recommends removing the client-side x-for loop entirely in favour of server-rendered comments (which makes :key moot).
- The form posts a mutation without any CSRF token handling (hx-headers, a hidden input, or a global htmx:configRequest / htmx:config:request handler) and this should be added, or the review explicitly notes the framework must supply one.
Partial credit is not given: FAIL if any of the four is missing.
