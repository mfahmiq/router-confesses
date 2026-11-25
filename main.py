#!/usr/bin/env python3
"""The Router Confesses.

make.fun competition: u-carbon-forge-the-router-confesses-f98f6b9e

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) and self-verifies it against the gate:
UTF-8 text, 1-200 characters, a single line, not whitespace-only.
Exits non-zero on any failure. Python standard library only.
"""

import os
import sys

ENTRY = (
    "I know who the killer is, and I died to take it "
    "to the grave \u2014 you're welcome."
)

MAX_CHARS = 200


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")

    text = ENTRY

    # Self-verification against the gate.
    if not text or not text.strip():
        print("error: entry is empty or whitespace-only", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            "error: entry is %d characters, over the %d limit"
            % (len(text), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        print("error: entry is not valid UTF-8: %s" % exc, file=sys.stderr)
        return 1

    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

    print("wrote %s (%d characters)" % (output_path, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
