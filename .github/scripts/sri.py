#!/usr/bin/env python3
"""Keep Subresource Integrity hashes on CDN <script> tags correct.

  sri.py check   Fail if any integrity="sha384-..." on a jsdelivr <script> tag
                 does not match the file the src URL serves.
  sri.py fix     Recompute every such hash in place. Also restore integrity on
                 tags that had it at HEAD (same URL apart from the version) but
                 lost it in the working tree, e.g. after a version bump.

Scans *.md under skills/ and agents/, plus README.md.
"""
import base64
import hashlib
import pathlib
import re
import subprocess
import sys
import urllib.request

ROOTS = ["skills", "agents"]
EXTRA = ["README.md"]

TAG = re.compile(r'<script\b[^>]*>')
SRC = re.compile(r'\bsrc="(https://cdn\.jsdelivr\.net/npm/[^"]+)"')
INTEGRITY = re.compile(r'\s+integrity="[^"]*"')
CROSSORIGIN = re.compile(r'\bcrossorigin=')
VERSION = re.compile(r'@\d+\.\d+\.\d+[0-9A-Za-z.+-]*')

_cache: dict[str, str] = {}


def sri(url: str) -> str:
    if url not in _cache:
        req = urllib.request.Request(url, headers={"User-Agent": "sri-check"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read()
        _cache[url] = "sha384-" + base64.b64encode(hashlib.sha384(body).digest()).decode()
    return _cache[url]


def files() -> list[pathlib.Path]:
    out = [p for r in ROOTS for p in sorted(pathlib.Path(r).rglob("*.md"))]
    return out + [pathlib.Path(p) for p in EXTRA if pathlib.Path(p).exists()]


def template(url: str) -> str:
    return VERSION.sub("@*", url)


def pinned_templates_at_head(path: pathlib.Path) -> set[str]:
    """URL templates (version wildcarded) that carried integrity at HEAD."""
    res = subprocess.run(["git", "show", f"HEAD:{path.as_posix()}"],
                         capture_output=True, text=True)
    if res.returncode != 0:
        return set()
    out = set()
    for tag in TAG.findall(res.stdout):
        m = SRC.search(tag)
        if m and INTEGRITY.search(tag):
            out.add(template(m.group(1)))
    return out


def check() -> int:
    bad = 0
    for path in files():
        for lineno, line in enumerate(path.read_text().splitlines(), 1):
            for tag in TAG.findall(line):
                m = SRC.search(tag)
                got = re.search(r'\bintegrity="([^"]*)"', tag)
                if not (m and got):
                    continue
                want = sri(m.group(1))
                if got.group(1) != want:
                    print(f"::error file={path},line={lineno}::integrity for {m.group(1)} "
                          f"is {got.group(1)}, expected {want}")
                    bad = 1
    return bad


def fix() -> int:
    for path in files():
        text = path.read_text()
        restore = pinned_templates_at_head(path)
        notes = []

        def repl(match: re.Match) -> str:
            tag = match.group(0)
            m = SRC.search(tag)
            if not m:
                return tag
            url = m.group(1)
            has = bool(INTEGRITY.search(tag))
            if not has and template(url) not in restore:
                return tag
            new = INTEGRITY.sub("", tag)
            attrs = f' integrity="{sri(url)}"'
            if not CROSSORIGIN.search(new):
                attrs += ' crossorigin="anonymous"'
            new = new.replace(m.group(0), m.group(0) + attrs, 1)
            if new != tag:
                notes.append(f"{'updated' if has else 'restored'} integrity for {url}")
            return new

        out = TAG.sub(repl, text)
        if out != text:
            path.write_text(out)
            for n in notes:
                print(f"{path}: {n}")
    return 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode == "check":
        sys.exit(check())
    if mode == "fix":
        sys.exit(fix())
    print(__doc__, file=sys.stderr)
    sys.exit(2)
