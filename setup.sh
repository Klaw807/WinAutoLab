#!/usr/bin/env bash
# keep the toolkit up-to-date and remind to rebind project
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd "$ROOT_DIR"

# keep the tool kit updated first
python3 toolkit/bin/tk sync-parent

# remind to rebind
TEMPLATE_REMOTE="git@github.com:Klaw807/project_template.git"
CURRENT_REMOTE="$(git remote get-url origin 2>/dev/null || true)"

if [[ "$CURRENT_REMOTE" == "$TEMPLATE_REMOTE" ]]; then
  cat <<EOF
This workspace is still bound to the template remote:
  $CURRENT_REMOTE

Please remove .git and rebind to your own project repository first:
  rm -rf .git
  git init
  git remote add origin <your-repo-url>

Then run setup.sh again.
EOF
  exit 1
fi

