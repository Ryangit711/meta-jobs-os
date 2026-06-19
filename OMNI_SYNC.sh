#!/bin/bash
# OMNI_SYNC.sh — Propagate meta-jobs-os AGENTS.md to all AI tool configs
# Follows the OMNI-gnostic principle from original JOBS-OS

META_DIR=$(dirname "$(readlink -f "$0")")
echo "[OMNI_SYNC] Syncing meta-jobs-os AGENTS.md to all tool configs..."

# Copy AGENTS.md to all tool config locations
declare -a TARGETS=(
    "$META_DIR/.opencode/AGENTS.md"
    "$META_DIR/CLAUDE.md"
    "$META_DIR/.cursorrules"
    "$META_DIR/.windsurfrules"
    "$META_DIR/.github/copilot-instructions.md"
    "$META_DIR/.clinerules/AGENTS.md"
    "$META_DIR/.kiro/AGENTS.md"
    "$META_DIR/.agents/AGENTS.md"
)

for target in "${TARGETS[@]}"; do
    mkdir -p "$(dirname "$target")"
    cp "$META_DIR/AGENTS.md" "$target"
    echo "[OK] → $target"
done

# Verify
echo "[OMNI_SYNC] Verifying all copies match..."
for target in "${TARGETS[@]}"; do
    if diff "$META_DIR/AGENTS.md" "$target" > /dev/null 2>&1; then
        echo "[MATCH] $target"
    else
        echo "[MISMATCH] $target — run copy again"
    fi
done

echo "[OMNI_SYNC] Complete. All tools see same kernel."
