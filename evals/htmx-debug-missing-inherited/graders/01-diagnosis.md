---
type: llm
---

PASS if the answer explains BOTH of the following and gives corrected code:
- In htmx 4 attributes no longer inherit implicitly, so the parent's hx-target / hx-swap / hx-headers are ignored by the child buttons and each button swaps into itself; the fix is the :inherited suffix on the parent (hx-target:inherited, hx-swap:inherited, hx-headers:inherited) or setting htmx.config.implicitInheritance = true, and it should note the CSRF header is also not being sent for the same reason.
- htmx 4 renamed the events, so the listener for htmx:afterSwap never fires; it must listen for htmx:after:swap (or load the htmx-2-compat extension as a bridge).
FAIL if either cause is missed, if the answer blames the server or a selector typo, or if it proposes 2.x-only fixes such as hx-disinherit.
