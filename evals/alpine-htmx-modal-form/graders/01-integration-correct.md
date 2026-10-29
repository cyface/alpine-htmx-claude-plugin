---
type: llm
---

PASS if the final HTML does ALL of the following:
- Alpine state for the modal is placed deliberately with respect to the htmx swap: EITHER the x-data element is outside the swap target so the open flag survives the swap, OR x-data sits on the swapped <li> and the answer explicitly relies on the re-rendered item resetting the state (and keeps the 422 response from replacing that element, for example via HX-Retarget or hx-target on the form). Placing x-data on the swapped element without acknowledging the reset is a FAIL.
- The form uses hx-post to /notes/42 (or templated id) and the successful response replaces #note-42 (hx-target="#note-42" or "closest li" with hx-swap="outerHTML", or equivalent).
- htmx event names in Alpine listeners, if any are used, are never camelCase (@htmx:afterRequest is wrong). Either the htmx 2.x kebab-case form (@htmx:after-request) or the htmx 4 colon form (@htmx:after:request) is acceptable, and the answer states or asks which htmx major the project uses, or shows both.
- The modal closes only on a successful response (by checking success in an event handler, or by the design where only the success response replaces the whole item) and stays open on a 422: the answer explains how the re-rendered form reaches the modal (htmx 4 swaps 422 by default and can route it with hx-status:422 or HX-Retarget; htmx 2 needs the response-targets extension, htmx.config.responseHandling, or a beforeSwap handler because 4xx responses are not swapped by default).
FAIL if camelCase htmx event names are used in Alpine listeners, if x-data is placed on the swapped element without accounting for the reset, if the modal closes regardless of success, or if the 422 case is ignored.
