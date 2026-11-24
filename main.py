#!/usr/bin/env python3
"""One Line, One Chill — entry program.

Writes a single sentence of horror (1-200 chars) to
$MAKEFUN_OUTPUT_DIR/entry.txt and self-checks the gate:
UTF-8 text, 1 to 200 characters, not only whitespace, one line.
Stdlib only, no network, deterministic.
"""

import os
import sys

ENTRY = (
    "The baby monitor finally went quiet, and then I heard my own voice "
    "humming the lullaby from the nursery I never entered."
)

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    text = ENTRY
    # Gate self-checks.
    assert isinstance(text, str)
    assert MIN_CHARS <= len(text) <= MAX_CHARS, (
        f"entry length {len(text)} outside {MIN_CHARS}-{MAX_CHARS}"
    )
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text.strip(), "entry must be a single line"
    assert text.strip().endswith("."), "entry must be one complete sentence"
    text.encode("utf-8")  # must be valid UTF-8

    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)

    # Read back and verify what was written.
    with open(path, "r", encoding="utf-8") as fh:
        written = fh.read()
    assert written == text, "written entry differs from intended entry"
    assert written.count("\n") == 0, "entry file must hold exactly one line"
    assert not written.endswith("\n"), "entry file must not end with a newline"
    assert "  " not in written, "entry must not contain double spaces"
    print(f"wrote {path}: {len(text)} chars")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
