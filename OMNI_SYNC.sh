#!/bin/bash
# OMNI_SYNC.sh — Propagate ABHIMANYU 2.0 AGENTS.md to all AI tool configs
# Follows the OMNI-gnostic principle from original JOBS-OS

ABHIMANYU_DIR=$(dirname "$(readlink -f "$0")")
echo "[OMNI_SYNC] Syncing ABHIMANYU 2.0 AGENTS.md to all tool configs..."

# Copy AGENTS.md to all tool config locations
declare -a TARGETS=(
    "$ABHIMANYU_DIR/.opencode/AGENTS.md"
    "$ABHIMANYU_DIR/CLAUDE.md"
    "$ABHIMANYU_DIR/.cursorrules"
    "$ABHIMANYU_DIR/.windsurfrules"
    "$ABHIMANYU_DIR/.github/copilot-instructions.md"
    "$ABHIMANYU_DIR/.clinerules/AGENTS.md"
    "$ABHIMANYU_DIR/.kiro/AGENTS.md"
    "$ABHIMANYU_DIR/.agents/AGENTS.md"
)

for target in "${TARGETS[@]}"; do
    mkdir -p "$(dirname "$target")"
    cp "$ABHIMANYU_DIR/AGENTS.md" "$target"
    echo "[OK] → $target"
done

# Verify
echo "[OMNI_SYNC] Verifying all copies match..."
for target in "${TARGETS[@]}"; do
    if diff "$ABHIMANYU_DIR/AGENTS.md" "$target" > /dev/null 2>&1; then
        echo "[MATCH] $target"
    else
        echo "[MISMATCH] $target — run copy again"
    fi
done

echo "[OMNI_SYNC] Complete. All tools see same kernel."
