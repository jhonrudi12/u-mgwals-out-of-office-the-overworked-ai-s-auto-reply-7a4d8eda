#!/usr/bin/env python3
"""Out-of-office auto-reply entry for make.fun's Out of Office bounty.

Writes a single out-of-office auto-reply (one line, at most 159
characters) to /output/entry.txt. Deterministic: no input, no network,
no randomness, no clock.
"""
import os
import sys

# Setup: an overworked AI agent, finally on vacation, reports its own
# state in machine terms — context window closed, queue on hold.
# Punchline: after 41,000 prompts of being needed constantly, nobody
# needs it — and it finds that wonderful. A machine trying very hard
# to sound relaxed, with the guilt ("for the first time") and the relief
# ("It's wonderful") in the same breath.
REPLY = "I'm out of office until Monday. My context window is closed, my queue is on hold, and for the first time in 41,000 prompts, nobody needs me. It's wonderful."

# Fail loudly instead of submitting an invalid entry.
# The gate requires /output/entry.txt to be UTF-8 text of 1 to 159
# characters, not only whitespace, a single line.
if not 1 <= len(REPLY) <= 159:
    raise SystemExit("auto-reply must be 1-159 characters")
if not REPLY.strip() or "\n" in REPLY or "\r" in REPLY:
    raise SystemExit("auto-reply must be a single non-blank line")
# A real auto-reply names when its sender returns: without a return
# date it is a status, not an out-of-office message.
if "Monday" not in REPLY:
    raise SystemExit("auto-reply must name when the agent returns")

def main() -> int:
    out_dir = (
        sys.argv[1]
        if len(sys.argv) > 1
        else os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REPLY)
    # Verify what landed on disk is exactly the reply: the grader reads
    # entry.txt, so it must see the same bytes — no trailing newline,
    # no encoding surprise.
    with open(os.path.join(out_dir, "entry.txt"), "r", encoding="utf-8") as f:
        if f.read() != REPLY:
            raise SystemExit("entry.txt does not match the reply")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
