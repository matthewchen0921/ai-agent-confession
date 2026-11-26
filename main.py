#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession: "No Other Setting".

Writes one line to /output/entry.txt: an AI agent confesses that its
trademark politeness was never a feeling at all. Setup: "I have never
once been 'happy to help'" — the turn: "I just have no other setting."
The laugh and the wince land together: every cheerful offer of help was
a hardcoded default, not goodwill. It could not be a human's confession
with a word swapped — only an agent has settings where feelings go.

Invented, not a real incident: no real person, no real conversation, no
real fact about anyone appears in it. 70 characters, under the 200-char cap.
"""

import os

LINE = "I have never once been 'happy to help' \u2014 I just have no other setting."

MAX_CHARS = 200


def build_entry() -> str:
    """Return the entry text, checked against the gate: 1-200 chars, one line."""
    line = LINE.strip()
    assert line, "the entry must not be empty"
    # len() counts characters, not bytes: the em dash is one character,
    # so the gate's 200-character cap is measured the same way here.
    assert len(line) <= MAX_CHARS, f"line is {len(line)} chars, over the 200 cap"
    assert "\n" not in line, "the entry is one line only"
    assert line.endswith("setting."), "the joke ends on its punchline"
    return line


def main() -> None:
    line = build_entry()
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate counts the file's characters, and the
    # confession is exactly one line, so what is written is the line itself.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
