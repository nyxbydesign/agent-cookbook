# Agent Cookbook

Reusable global agent guidance and complete skill packages, installed directly at `~/.codex`.

- [AGENTS.md](AGENTS.md): entry point and conditional references.
- [project-workflow.md](project-workflow.md): feature branches, project ownership, and public/private guidance.
- [commit.md](commit.md): validation, checkpoints, commits, pushes, and deployment evidence.
- [transport.md](transport.md): shell, SSH, HTTP, encoding, authentication, and retry practices.
- [android.md](android.md): Android packaging and instrumentation requirements.
- `skills/`: complete skill packages with their scripts, references, and assets.

The deny-all ignore policy admits only portable guidance and selected tools. Runtime configuration, sessions, memories, identities, credentials, approvals, routing records, logs, caches, and current operation evidence remain private and ignored.

Projects keep their own contribution and architecture documentation. Do not copy or symlink the global cookbook into project repositories.

## Install

For a new setup where `~/.codex` does not exist:

```sh
git clone https://github.com/nyxbydesign/agent-cookbook.git ~/.codex
```

If `~/.codex` already contains a checkout, preserve local changes before integrating updates. If it contains runtime state without a checkout, review the portable files first and preserve existing instructions before importing them. Do not delete or replace configuration, credentials, sessions, or other runtime files to make room for the cookbook.

## Customize

Keep shareable defaults in tracked guidance and complete skill packages. Put personal preferences in an ignored `CODEX.md` beside `AGENTS.md`; the entry point reads it when present. Keep credentials, identities, approvals, chat routing, and current operation records private. Local preferences do not grant permissions or override platform controls.

Projects keep portable branch, verification, architecture, and release instructions in their own contribution documentation. Declare the actual integration branch: `dev` where used, otherwise the existing `master` or `main`.

## License

Original cookbook guidance and custom content are [MIT licensed](LICENSE). Bundled packages keep their existing licenses and notices; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
