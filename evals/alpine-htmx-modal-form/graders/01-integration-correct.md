---
type: llm
---

PASS if the final HTML does ALL of the following:
- Alpine state for the modal (x-data with the open flag) lives on an element that is NOT the htmx swap target, so the state survives the swap.
- The form uses hx-post to /notes/42 (or templated id) and targets #note-42 with hx-swap="outerHTML" (or equivalent) so the returned <li> replaces the list item.
- When listening to htmx events from Alpine, the event names are written in kebab-case (for example @htmx:after-request, @htmx:after-swap, @htmx:response-error), never camelCase like @htmx:afterRequest.
- The modal closes only on a successful response (for example by checking $event.detail.successful in @htmx:after-request, or by handling the 422 case so the form stays open), and the answer explains how the 422 form re-render is swapped into the modal (hx-target on the form, response-targets extension, or htmx.config.responseHandling / a beforeSwap handler so 422 is swapped).
FAIL if camelCase htmx event names are used in Alpine listeners, if x-data is placed on the element being swapped, if the modal closes regardless of success, or if the 422 case is ignored.
