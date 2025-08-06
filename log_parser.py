#!/usr/bin/env python3
import subprocess
import json
import sys

def get_git_logs(limit=10):
    """Get the latest git logs as a list of dicts."""
    try:
        log_format = "%H|%an|%ad|%s"
        cmd = ["git", "log", f"--pretty=format:{log_format}", f"-{limit}", "--date=iso"]
        raw_output = subprocess.check_output(cmd, text=True)
        commits = []
        for line in raw_output.split("\n"):
            commit_hash, author, date, message = line.split("|", 3)
            commits.append({
                "hash": commit_hash,
                "author": author,
                "date": date,
                "message": message
            })
        return commits
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    logs = get_git_logs(limit)
    print(json.dumps(logs, indent=2))
