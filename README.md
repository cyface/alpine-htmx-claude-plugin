# alpine-htmx

A Claude Code plugin with expert guidance for **Alpine.js v3** and **htmx** (both the 2.x line and htmx 4), the lightweight hypermedia-driven frontend stack. Two skills teach Claude the frameworks in depth; one agent reviews what gets written.

## Install

```text
/plugin install alpine-htmx --marketplace cyface/alpine-htmx-claude-plugin
```

That single command works on Claude Code 2.1.275 or later. On older versions, add the marketplace first:

```text
/plugin marketplace add cyface/alpine-htmx-claude-plugin
/plugin install alpine-htmx@cyface
```

From a shell: `claude plugin marketplace add cyface/alpine-htmx-claude-plugin && claude plugin install alpine-htmx@cyface`. To try a local checkout without installing: `claude --plugin-dir ./alpine-htmx-claude-plugin`.

## What's included

### Skills

| Skill | Loads when you… | Covers |
|-------|-----------------|--------|
| `alpine-js` | write `x-data`, `x-show`, `@click`, ask for a modal, dropdown, tabs, toast, wizard, filter, or mention Alpine stores, plugins, or the CSP build | All 18 core directives and 9 magics with current modifiers, `Alpine.data`/`store`/`bind`, the nine official plugins (Focus, Collapse, Intersect, Resize, Persist, Mask, Anchor, Morph, Sort), the rewritten CSP build, accessible component patterns |
| `htmx` | write `hx-get`/`hx-post`/`hx-swap`/`hx-trigger`, ask for AJAX without a framework, active search, infinite scroll, polling, SSE/WebSockets, `HX-*` headers, CSRF, or a 2→4 migration | Both supported lines side by side: attributes, swap and trigger grammar, `<hx-partial>`, OOB swaps, events, config, headers, extensions, security, server-side checklist, and a step-by-step htmx 2 to 4 migration guide |

Both skills cover **Alpine + htmx integration**: which library owns what, keeping Alpine state across swaps, and the event-name differences between htmx 2 (`@htmx:after-request`) and htmx 4 (`@htmx:after:request`).

### Agent

| Agent | Runs when… | Does |
|-------|------------|------|
| `alpine-htmx-reviewer` | proactively after Alpine/htmx markup is written, or on request | Detects the htmx line in use, then reviews for anti-patterns, accessibility, security (XSS, CSRF, CSP), and integration mistakes, reporting by severity with fixes. Has both skills preloaded. |

### Evals

`evals/` holds four cases for `claude plugin eval` (accessible modal, debounced active search, Alpine+htmx modal form, reviewer catching XSS/CSRF). Run them from the repo root:

```bash
claude plugin eval .            # runs each case with and without the plugin and reports the delta
claude plugin validate --strict . # structural checks, no model calls
```

Eval runs call the model with your credentials and cost real usage.

## Framework versions covered

| Framework | Version | Notes |
|-----------|---------|-------|
| Alpine.js | 3.17.x | Latest stable; no v4 exists. Includes `x-modelable`, Anchor/Resize plugins, `Alpine.deferInit`, the new CSP evaluator. |
| htmx 2.x | 2.0.11 | npm `latest`; supported indefinitely. Includes `<hx-partial>` (2.0.11) and the `inherit` keyword. |
| htmx 4 | 4.0.0 | Stable since 2026-08-28; fetch-based, explicit `:inherited` attribute inheritance, `htmx:phase:action` events, built-in morphing, `hx-status`, no `hx-ext`, no 286. |

## Repository layout

```
.claude-plugin/
├── plugin.json          # manifest
├── marketplace.json     # self-hosted marketplace entry for one-step install
└── icon.png
skills/
├── alpine-js/
│   ├── SKILL.md
│   └── references/      # alpine-directives.md, alpine-plugins.md, alpine-patterns.md
└── htmx/
    ├── SKILL.md
    └── references/      # htmx-attributes.md, htmx-patterns.md, htmx-4-migration.md
agents/
└── alpine-htmx-reviewer.md
evals/                   # claude plugin eval cases
```

## Privacy

The plugin is static Markdown only: no hooks, no MCP servers, no network calls, no telemetry. See [PRIVACY.md](PRIVACY.md).

## License

MIT
