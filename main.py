#!/usr/bin/env python3
# vending-pickup-line -- one pickup line, spoken by a vending machine.
#
# The contest asks for a single line (200 characters max) that a vending
# machine would use on a passing human. This script keeps that line in one
# place and drops it, byte for byte, into /output/entry.txt so the judge
# can read it. No network, no arguments, no extra output files.
#
# Run it with `python3 main.py`; the file it leaves behind is the entry.

import sys
from pathlib import Path

# The whole entry. One line, 107 characters, no trailing newline on disk.
PICKUP_LINE = "Are you exact change? Because every time you walk by, my coils do a little spin and I drop something extra."

MAX_CHARS = 200
DESTINATION = Path("/output/entry.txt")


def check_line(line):
    """Refuse anything that is not exactly one short, non-blank line."""
    stripped = line.strip()
    if not stripped:
        raise ValueError("pickup line must not be blank")
    if len(line) > MAX_CHARS:
        raise ValueError("pickup line is over the 200-character limit")
    for bad in ("\n", "\r"):
        if bad in line:
            raise ValueError("pickup line must fit on a single line")
    return line


def main(argv=None):
    """Validate the line, then write it out verbatim and exit cleanly."""
    del argv  # this program takes no arguments
    line = check_line(PICKUP_LINE)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(line, encoding="utf-8", newline="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
