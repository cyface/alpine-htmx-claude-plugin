---
type: llm
---

PASS if the final HTML snippet does ALL of the following:
- The modal container has role="dialog" (or is a native <dialog> element) and aria-modal="true", and a label via aria-labelledby or aria-label.
- Focus is trapped while open, using x-trap from the @alpinejs/focus plugin (or an equivalent documented approach such as a native <dialog> opened with showModal()).
- Pressing Escape closes the modal (for example @keydown.escape.window) and focus is returned to the triggering button on close.
- Clicking the backdrop closes it without clicks inside the panel closing it (for example @click.outside on the panel, or @click on the overlay with @click.stop on the panel).
- The snippet uses x-cloak or an equivalent and mentions the required [x-cloak] CSS, or explains how the flash of unstyled content is avoided.
FAIL if any of: no dialog role or aria-modal, no focus trapping, no Escape handling, focus is not returned to the trigger, or the focus plugin is used without a script tag that loads it before Alpine core.
