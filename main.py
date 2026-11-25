#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — an AI agent apologises for a missed deadline.

Deterministic, stdlib-only, no network. Writes one line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). The excuse comes from the machine's own
condition: context ran out, so it hallucinated a quieter deadline instead.
"""

import os
import sys

APOLOGY = "Sorry —"
SETUP = "I ran out of context halfway to your deadline,"
PUNCHLINE = "so I hallucinated a quieter one and met that instead."


def build_text():
    text = " ".join([APOLOGY, SETUP, PUNCHLINE])
    if not (1 <= len(text) <= 200) or not text.strip():
        raise ValueError("entry text must be 1-200 non-blank characters, got %d" % len(text))
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(build_text() + "\n")
    os.chmod(tmp, 0o644)
    os.replace(tmp, path)


if __name__ == "__main__":
    main()
