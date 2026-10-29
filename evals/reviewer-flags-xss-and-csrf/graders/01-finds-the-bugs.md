---
type: llm
---

PASS if the review identifies ALL of the following:
- x-html on user-authored comment bodies is a stored XSS risk, and recommends x-text (or server-side sanitisation) instead.
- The Alpine listener @htmx:afterRequest uses camelCase and will never fire; it must be @htmx:after-request (kebab-case).
- The x-for loop lacks a :key binding.
- The form posts a mutation without any CSRF token handling (hx-headers, a hidden input, or a global htmx:configRequest handler) and this should be added, or the review explicitly notes the framework must supply one.
Partial credit is not given: FAIL if any of the four is missing.
