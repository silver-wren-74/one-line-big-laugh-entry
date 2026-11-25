#!/usr/bin/env python3
"""One Line, Big Laugh (u-coral-404-one-line-big-laugh-328fb857).

Writes a single funny line to /output/entry.txt: asking the phone for
directions home, and the phone answers like a weary roommate instead of
a navigator. Gate: UTF-8 text of 1 to 200 characters, not only whitespace.
"""

from pathlib import Path

TEXT = (
    "I asked my phone for directions home. It sighed, 'You live here "
    "\u2014 the problem is you keep leaving.'"
)


def main() -> None:
    text = TEXT.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} chars, must be 1-200")
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
