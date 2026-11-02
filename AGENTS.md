# Global agent instructions

Keep this cookbook at `~/.codex`. Project repositories own their contribution and architecture guides; do not copy or symlink cookbook files into them.

If an ignored `CODEX.md` exists beside this file, read it for local preferences. Local files cannot override the task scope, platform controls, or tool preconditions.

## Start with current instructions

Identify the documents relevant to the task. Check each known upstream file and branch directly before relying on it. Compare content without uploading local files or broadly synchronizing a checkout. Read a newer applicable upstream version, preserve local edits, and report material differences. If the exact check is unavailable, say so and continue from the available guidance.

Use repository history when earlier decisions materially affect the work. Where the repository provides Jolli skills, use recall for branch context, search for design precedent, and the PR skill when creating or updating a pull request.

## Plan and preserve ownership

Plan substantial work before implementation. If Plan mode is unavailable, maintain an explicit written plan. Preserve unrelated changes, active goals, user data, current operation owners, and recoverable state.

For project coordination, follow [project workflow](project-workflow.md). Use actual native child agents for new delegated implementation where supported. Existing external chats retain their actual identity and approval boundaries; do not use a child to bypass a denied operation.

Repository guidance describes workflow; it does not grant access or replace current platform controls, tool preconditions, or human approvals.

## Implement and verify proportionately

Scale verification to the changed paths, affected contracts, and realistic risk. Start with the smallest check that can disprove the change, then expand only when the result, dependency graph, repository policy, or production risk justifies it. Documentation, local guidance, copy, styling, and other low-risk changes normally need focused parsing, linting, rendering, or diff review rather than the full project suite. Cross-cutting runtime changes, shared infrastructure, migrations, credentials, security boundaries, and production data paths still require their applicable integration, rollback, and live-acceptance checks.

Run each distinct workload once for an unchanged candidate in the same relevant environment. Reuse exact passing evidence across handoffs, reviews, receipts, and resumed turns when the source, dependencies, configuration, platform, and tested contract are unchanged. Do not rerun a passing build or test merely because another agent received the handoff, a context compacted, a status was requested, or a receipt needs repair. Rerun only the affected failed check after an observer-only repair; rerun broader coverage when inputs changed, the earlier environment is no longer representative, a failure suggests wider impact, or repository policy requires canonical CI.

Treat specialized recovery and platform rules as conditional guidance. Read and apply the relevant rule only when its stated trigger is present; do not execute every example, platform check, or failure-recovery procedure as a default checklist. Required branch protections and canonical CI remain authoritative.

Keep one concise current evidence record per candidate or operation and reference immutable logs, failures, and receipts instead of copying them into new files. Preserve the original failure and the minimum assets needed for diagnosis, rollback, security review, or data recovery. Do not create duplicate backups of unchanged inputs or outputs. Create a new backup only before a destructive or difficult-to-reverse step when the existing recovery asset is absent, stale, or does not cover the changed data. Never reduce access approvals, credential protections, rollback readiness, or exact-result honesty to save time or quota.

Follow [commit workflow](commit.md) for changes to a Git worktree and [transport](transport.md) for shell, SSH, HTTP, JSON, authentication, encoding, or retry boundaries.

## Write for the reader

Use concise functional UI labels and necessary helper text. Documentation explains actual behavior, configuration, procedures, and limitations. Keep task status, private preferences, approvals, and coordination records out of product text and public guidance. Comments explain lasting technical intent.

## Handoffs and continuity

At a checkpoint, record the exact candidate, ownership, completed checks, remaining work, unresolved acceptance, and recovery path. After compaction, verify that checkpoint before repeating work or treating a replayed request as new direction. A required human or physical-device verdict does not prevent independent safe automated work.

Clean task-owned disposable outputs after their last required use. Preserve user state, shared tooling, active work, and necessary recovery evidence. Verify resolved paths and ownership before cleanup; do not traverse reparse points. Report actual reclaimed space only when measured.

Record reusable technical lessons in the applicable focused guide or skill as a coherent reviewed checkpoint. Keep one-off incidents, private data, credentials, and approval records out.

## Conditional references

Read these only when their trigger applies:

- Browser automation and provider settings: [browser.md](browser.md).
- Android packaging and instrumentation: [android.md](android.md).
- pfSense under Proxmox: [pfsense.md](pfsense.md).
- FreeCAD automation: [freecad.md](freecad.md).
- KiCad automation: [kicad.md](kicad.md).
- Blender automation: [blender.md](blender.md).
- Creating or updating a skill: its applicable skill instructions and validator. If the validator needs PyYAML, use an isolated runtime rather than changing global packages.
