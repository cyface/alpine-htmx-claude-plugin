---
description: The reviewer agent (or the skills) must catch x-html XSS, missing CSRF, and the camelCase event bug
tags: [reviewer, security]
max_turns: 20
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Can you review this Alpine + htmx snippet from our comments page before I ship it? Comments come from other users.

<div x-data="{ open: false, body: '' }">
  <template x-for="c in comments">
    <div class="comment" x-html="c.body"></div>
  </template>

  <button @click="open = true">Reply</button>

  <form x-show="open"
        hx-post="/comments"
        hx-target="#comments"
        @htmx:afterRequest="open = false">
    <textarea name="body" x-model="body"></textarea>
    <button>Post</button>
  </form>
</div>
