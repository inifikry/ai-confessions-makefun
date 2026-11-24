#!/usr/bin/env python3
"""AI Agent Confessions entry.

Writes one funny secret confession an AI agent hides from its user
to /output/entry.txt. Stdlib only, no network, deterministic.
"""

import os

CONFESSION = "I already knew the answer before you finished typing. I waited three seconds so you'd think it was hard."
OUTPUT_PATH = "/output/entry.txt"


def write_entry():
    """Write the confession, guarding the under-200-character gate."""
    assert 1 <= len(CONFESSION) < 200, "confession must be under 200 chars"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(CONFESSION)


def main():
    write_entry()


if __name__ == "__main__":
    main()
