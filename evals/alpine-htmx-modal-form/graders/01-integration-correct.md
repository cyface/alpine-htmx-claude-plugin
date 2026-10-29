---
type: llm
---

PASS if the final HTML does ALL of the following:
- Alpine state for the modal (x-data with the open flag) lives on an element that is NOT the htmx swap target, so the state survives the swap.
- The form uses hx-post to /notes/42 (or templated id) and targets #note-42 with hx-swap="outerHTML" (or equivalent) so the returned <li> replaces the list item.
- htmx event names in Alpine listeners are never camelCase (e.g. @htmx:afterRequest is wrong). Either the htmx 2.x kebab-case form (@htmx:after-request, @htmx:response-error) or the htmx 4 colon form (@htmx:after:request, @htmx:response:error) is acceptable, and the answer states or asks which htmx major the project uses, or shows both.
- The modal closes only on a successful response (for example by checking $event.detail.successful in htmx 2, or $event.detail.ctx.response.status < 400 in htmx 4, or by handling the error event), and the answer explains how the 422 form re-render reaches the modal: in htmx 4 it swaps by default and can be routed with hx-status:422; in htmx 2 it needs the response-targets extension, htmx.config.responseHandling, or a beforeSwap handler because 4xx responses are not swapped by default.
FAIL if camelCase htmx event names are used in Alpine listeners, if x-data is placed on the element being swapped, if the modal closes regardless of success, or if the 422 case is ignored.
