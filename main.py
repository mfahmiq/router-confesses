#!/usr/bin/env python3
"""The Router Confesses.

make.fun competition: u-carbon-forge-the-router-confesses-f98f6b9e

Writes the entry line verbatim to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) and prints it to stdout.

The entry is validated against the competition gate before any
write: UTF-8 text, 1-200 characters, a single line, not
whitespace-only. Exits non-zero on any failure.
Python standard library only.
"""

import os
import sys

ENTRY = (
    "I know who the killer is, and I died to take it "
    "to the grave \u2014 you're welcome."
)

MAX_CHARS = 200


def validate(entry: str) -> None:
    """Enforce the competition gate; raise ValueError on failure."""
    if not entry or not entry.strip():
        raise ValueError("entry is empty or whitespace-only")
    if len(entry) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit"
            % (len(entry), MAX_CHARS)
        )
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    try:
        entry.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError("entry is not valid UTF-8: %s" % exc)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")

    try:
        validate(ENTRY)
    except ValueError as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 1

    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    # Read-back verification: the file on disk must be exactly ENTRY.
    with open(output_path, "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        print(
            "error: read-back mismatch in %s" % output_path,
            file=sys.stderr,
        )
        return 1

    print(ENTRY, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
