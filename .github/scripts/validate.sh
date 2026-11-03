#!/usr/bin/env bash
# Plugin checks shared by validate.yml and the framework-versions upgrade job.
# Runs every check and exits non-zero if any failed. Needs node (npx), jq, python3.
set -uo pipefail
cd "$(dirname "$0")/../.."
fail=0

echo "::group::Structural checks (claude plugin validate --strict)"
npx -y @anthropic-ai/claude-code plugin validate --strict . || { echo "::error::plugin validate --strict failed"; fail=1; }
echo "::endgroup::"

echo "::group::Pinned versions in skills match versions.json"
alp=$(jq -r '.alpinejs.latest' versions.json)
h2=$(jq -r '."htmx.org".latest' versions.json)
h4=$(jq -r '."htmx.org".next' versions.json)
for pin in "alpinejs@$alp" "@alpinejs/focus@$alp" "htmx.org@$h2" "htmx.org@$h4"; do
  if ! grep -rq --include='*.md' -- "$pin" skills; then echo "::error::no skill pins $pin"; fail=1; fi
done
# Catch stale pins for the same packages at other versions
while read -r pin; do
  case "$pin" in
    alpinejs@"$alp"|@alpinejs/*@"$alp"|htmx.org@"$h2"|htmx.org@"$h4") ;;
    *) echo "::error::stale pin $pin in skills/"; fail=1 ;;
  esac
done < <(grep -rhoE --include='*.md' '(alpinejs|@alpinejs/[a-z]+|htmx\.org)@[0-9]+\.[0-9]+\.[0-9]+' skills | sort -u)
echo "::endgroup::"

echo "::group::SRI hashes match the CDN files"
python3 .github/scripts/sri.py check || fail=1
echo "::endgroup::"

exit $fail
