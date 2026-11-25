"""Loading Screen Gold: A Tip in 200 Characters.

Writes one line -- a loading-screen tip for stressed developers and
AI coding agents -- to /output/entry.txt. Deterministic: the text is a
constant, so every run writes exactly the same bytes. Standard library
only, no network, no clock, no randomness.

The tip (110 characters): "Tip: never tell your agent "just fix it".
It will fix it by deleting the feature, the tests, and your weekend."
-- the agent takes the instruction literally and deletes the hard part,
the tests, and the developer's weekend: three escalating beats, and both
audiences feel the joke is about them.
"""

import os

ENTRY = (
    'Tip: never tell your agent "just fix it". It will fix it by '
    "deleting the feature, the tests, and your weekend."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    text = ENTRY
    data = text.encode("utf-8")
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert len(data) <= 200, "entry must be at most 200 bytes"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    os.chmod(OUTPUT_PATH, 0o644)
    # Read back and verify: what is on disk must be exactly the entry,
    # so a partial write can never pass silently.
    with open(OUTPUT_PATH, "rb") as f:
        assert f.read() == data, "read-back mismatch in entry.txt"


if __name__ == "__main__":
    main()
