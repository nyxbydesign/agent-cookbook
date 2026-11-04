#!/usr/bin/env python3
"""Fail unless a cookbook source checkout is clean and fully pushed."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def git(repo: Path, *args: str, check: bool = True) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if check and result.returncode:
        detail = result.stderr.strip() or result.stdout.strip() or args[0]
        raise RuntimeError(detail)
    return result.stdout.strip()


def main() -> int:
    repo = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd().resolve()
    top = Path(git(repo, "rev-parse", "--show-toplevel")).resolve()
    if top != repo:
        raise RuntimeError(f"run from the source checkout root: {top}")

    status = git(repo, "status", "--porcelain=v2", "--untracked-files=all")
    branch = git(repo, "symbolic-ref", "--quiet", "--short", "HEAD", check=False)
    if not branch:
        raise RuntimeError("detached HEAD has no publishable branch")
    upstream = git(repo, "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{upstream}", check=False)
    if not upstream:
        raise RuntimeError(f"branch {branch} has no upstream")
    upstream_ref = git(repo, "rev-parse", "--symbolic-full-name", "@{upstream}")
    prefix = "refs/remotes/"
    if not upstream_ref.startswith(prefix) or "/" not in upstream_ref[len(prefix) :]:
        raise RuntimeError(f"unsupported upstream ref: {upstream_ref}")
    remote, remote_branch = upstream_ref[len(prefix) :].split("/", 1)
    live = git(repo, "ls-remote", "--exit-code", "--heads", remote, f"refs/heads/{remote_branch}")
    live_fields = live.split()
    if len(live_fields) != 2:
        raise RuntimeError(f"could not resolve live upstream: {upstream}")
    live_head = live_fields[0]

    counts = git(repo, "rev-list", "--left-right", "--count", f"HEAD...{upstream}").split()
    if len(counts) != 2:
        raise RuntimeError("could not compare HEAD with its upstream")
    ahead, behind = map(int, counts)
    unpushed = git(repo, "rev-list", "HEAD", "--not", "--remotes")

    report = {
        "repo": str(repo),
        "branch": branch,
        "upstream": upstream,
        "remote": remote,
        "remoteHead": live_head,
        "commit": git(repo, "rev-parse", "HEAD"),
        "clean": not status,
        "ahead": ahead,
        "behind": behind,
        "unpushedCommits": len(unpushed.splitlines()) if unpushed else 0,
    }
    print(json.dumps(report, sort_keys=True))
    return 0 if report["clean"] and ahead == 0 and behind == 0 and not unpushed and report["commit"] == live_head else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        raise SystemExit(2)
