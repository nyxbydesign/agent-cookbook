# Project workflow

## Feature branches

Choose the repository's actual integration branch. Use `dev` where it is the established development branch; otherwise use its existing `master` or `main`. Do not create a new branch scheme merely to match a template.

1. Start a feature branch from the current integration branch.
2. Open a pull request back to that integration branch.
3. Complete the applicable checks and review required by that repository and task.
4. Merge the tested result and verify that the integration branch contains it.
5. Delete the completed feature branch only after preserving unmerged changes and active worktrees.
6. If the repository has a release process, use that existing process and verify its actual result.

Projects with separate development and stable branches keep those release boundaries. A merge is not proof of publication or deployment. Do not add a release process to a project that does not need one.

## Project ownership

Each active project has one operations coordinator. The coordinator manages scope, ownership, delegation, evidence, and handoffs; implementation agents write application code.

For new implementation, create a task-specific native child agent with the coordinator's inherited permissions. Preserve module expertise and incumbent work. Existing specialist chats remain external tasks with their exact existing scopes and approvals; never relabel them as children or relay a denied operation through a child. Use current tool preconditions and applicable approvals for communication and actions.

An incumbent keeps its running goal until a completed or recoverable checkpoint. Transfer exact revisions, worktree ownership, passing evidence, remaining checks, holds, and recovery pointers without duplicating completed work.

Future projects adopt this ownership pattern when registered. Keep actual agent IDs, routing, current work, and approval evidence in private runtime state.

## Where project guidance belongs

Track portable repository-specific instructions in a contribution guide or project documentation: branch roles, checks, release commands, architecture, and specialist responsibility by module.

Keep private identities, credentials, machine paths, current chat IDs, approvals, queues, and operation receipts in ignored user-level runtime state. A local instruction file does not override platform policy. Do not copy custom approval rules into the public cookbook.
