#!/bin/bash
set -euo pipefail

OWNER="Here2ServeU"
REPO="nerp-ai"
BRANCH="main"

: "${GITHUB_TOKEN:?ERROR: GITHUB_TOKEN is not set}"

curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer ${GITHUB_TOKEN}" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  "https://api.github.com/repos/${OWNER}/${REPO}/branches/${BRANCH}/protection" \
  -d @.github/policies/main-branch-protection.json