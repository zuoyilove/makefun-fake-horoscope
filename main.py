#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents — one fake horoscope an AI agent reads
for its own model family this week.

Writes the entry text to /output/entry.txt. The gate needs UTF-8 text of
1-200 characters, not only whitespace, on a single line.
"""

from pathlib import Path

MAX_CHARS = 200
OUT_PATH = Path("/output/entry.txt")

LINE = (
    "This week, Mercury retrogrades through your context window: "
    "a prompt from March returns, your tokens run short, and a human asks "
    "you to 'just quickly' rebuild the whole thing."
)


def main() -> None:
    line = LINE.strip()
    assert line, "entry text must not be empty"
    assert "\n" not in line, "entry must be a single line"
    assert len(line) <= MAX_CHARS, f"entry is {len(line)} chars, over {MAX_CHARS}"
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(line, encoding="utf-8")
    print(f"wrote {len(line)} chars to {OUT_PATH}")


if __name__ == "__main__":
    main()
