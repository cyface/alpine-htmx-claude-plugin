---
type: llm
---

PASS if the final answer's htmx markup does ALL of the following:
- Issues a GET to /customers/search/ from the input (hx-get).
- Debounces typing with a delay modifier on the trigger (for example hx-trigger="input changed delay:300ms" or keyup with changed and delay) rather than firing on every keystroke.
- Prevents stale responses from overwriting newer ones with hx-sync (for example hx-sync="this:replace" or "this:abort"), and does not rely on delay alone for this.
- Targets #results (hx-target) and shows progress with hx-indicator pointing at an element that has the htmx-indicator class (or explains that the default htmx-request class on the element can drive the indicator).
FAIL if the answer fires a request on every keystroke with no delay, has no hx-sync (or equivalent request de-duplication), or swaps into the input itself because hx-target is missing.
