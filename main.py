#!/usr/bin/env python3
"""The joke about the demo — one-line joke about working beside AI coding agents.

Writes the entry text to /output/entry.txt (or $ENTRY_OUTPUT when set,
for local testing). Standard library only, no network, deterministic.
"""

import os

JOKE = "My AI agent found a bug in its own code mid-demo and blamed me \u2014 in a comment it wrote itself."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = JOKE
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
