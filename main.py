#!/usr/bin/env python3
"""Real-Life Patch Notes entry: one funny one-line patch note.

Writes the note to /output/entry.txt (UTF-8, 1-160 chars, single line).
"""

import os

MAX_CHARS = 160  # kit gate: /output/entry.txt must be 1-160 UTF-8 chars

NOTE = "v3.0.1: fixed a bug where the bladder only reports 'urgent' after you are home and the keys are already in the door."


def main() -> None:
    assert 1 <= len(NOTE) <= MAX_CHARS, f"note is {len(NOTE)} chars, must be 1-160"
    assert NOTE.strip() == NOTE and "\n" not in NOTE, "note must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(NOTE)
    print(f"wrote {len(NOTE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
