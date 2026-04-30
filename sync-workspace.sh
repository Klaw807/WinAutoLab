#!/usr/bin/env bash
# Keep shared workspace submodules up to date and stage pointer changes.
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$ROOT_DIR/toolkit/shell/load.sh"

cd "$ROOT_DIR"

DRY_RUN=0

if [[ "${1:-}" == "--dry-run" ]]; then
  DRY_RUN=1
elif [[ $# -gt 0 ]]; then
  echo "Usage: bash sync-workspace.sh [--dry-run]" >&2
  exit 1
fi

TEMPLATE_REMOTE="git@github.com:Klaw807/project_template.git"
CURRENT_REMOTE="$(git remote get-url origin 2>/dev/null || true)"

ensure_rebound_remote() {
  if [[ "$CURRENT_REMOTE" == "$TEMPLATE_REMOTE" ]]; then
    if [[ $DRY_RUN -eq 1 ]]; then
      log_info "Dry run note: workspace is still bound to the template remote: $CURRENT_REMOTE"
      return
    fi

    cat <<EOF
This workspace is still bound to the template remote:
  $CURRENT_REMOTE

Please remove .git and rebind to your own project repository first:
  rm -rf .git
  git init
  git remote add origin <your-repo-url>

Then run sync-workspace.sh again.
EOF
    exit 1
  fi
}

git_sync_and_stage "toolkit" "main" "$ROOT_DIR" "$DRY_RUN"
git_sync_and_stage "agent-workflow" "main" "$ROOT_DIR" "$DRY_RUN"
ensure_rebound_remote

if [[ $DRY_RUN -eq 1 ]]; then
  log_success "Dry run complete"
else
  log_success "Workspace dependencies updated and staged"
fi
