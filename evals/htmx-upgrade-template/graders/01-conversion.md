---
type: llm
---

PASS if the converted output does ALL of the following:
- Adds :inherited to the body-level attributes that are meant for descendants: hx-headers:inherited and hx-boost:inherited.
- Renames hx-disabled-elt to hx-disable on the form, and renames the map wrapper's hx-disable to hx-ignore (and does not confuse the two).
- Renames the event listeners to htmx:config:request and htmx:response:error, and rewrites the handler bodies to use e.detail.ctx (ctx.request.headers for the timezone header, ctx.response.status instead of e.detail.xhr.status).
- Addresses the polling div: explains that a 286 response no longer stops polling in htmx 4 and proposes load polling (the server omits the trigger when done) or a filter.
- Mentions the server-side changes: 4xx/5xx responses now swap by default (so error pages need handling via noSwap config, hx-status, or proper fragments), the HX-Trigger request header is now HX-Source, and HX-Trigger-After-Swap/Settle are gone.
FAIL if hx-disable/hx-ignore are swapped the wrong way, if :inherited is omitted on hx-headers, if 2.x event names remain, or if the answer rewrites nothing and only lists generic advice.
