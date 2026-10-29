---
type: llm
---

PASS if the final HTML snippet does ALL of the following:
- The modal container has role="dialog" or role="alertdialog" (or is a native <dialog> element), aria-modal="true", and a label via aria-labelledby or aria-label.
- Focus is trapped while open, using x-trap from the @alpinejs/focus plugin (or an equivalent documented approach such as a native <dialog> opened with showModal()).
- Pressing Escape closes the modal (for example @keydown.escape on the dialog or .window).
- Focus returns to the triggering button on close: either explicitly (for example $refs.trigger.focus()) or by relying on x-trap's automatic restore, provided the answer says so.
- Clicking the backdrop closes it without clicks inside the panel closing it (for example @click.outside on the panel, @click.self on the overlay, or @click on a separate backdrop element).
- The snippet uses x-cloak and includes or mentions the required [x-cloak] CSS, or otherwise explains how the flash of unstyled content is avoided.
FAIL if any of: no dialog/alertdialog role or no aria-modal, no focus trapping, no Escape handling, focus return is neither implemented nor mentioned, or the focus plugin is used without a script tag that loads it before Alpine core.
