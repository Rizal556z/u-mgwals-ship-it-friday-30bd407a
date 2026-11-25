"""Ship It Friday — make.fun Growth entry.

Writes one line: the funniest git commit message an AI coding agent
writes in the moment before it breaks production on a Friday.

Gate: /output/entry.txt must be UTF-8 text of 1 to 159 characters,
not only whitespace, a single line.
"""

import os

ENTRY = (
    "feat: ship it Friday \u2014 all tests green, vibes immaculate, "
    "rollback plan is just confidence"
)

MAX_CHARS = 159


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert len(text) <= MAX_CHARS, f"entry is {len(text)} chars, over {MAX_CHARS}"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip() == text, "entry must not be only whitespace"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Second-pass validation gate: re-read what was actually written and
    # check the gate against the file itself, not just the in-memory string.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    written = raw.decode("utf-8")
    assert written == text, "written file differs from entry text"
    assert 1 <= len(written) <= MAX_CHARS, "file fails char gate"
    assert written.strip(), "file must not be only whitespace"
    assert "\n" not in written and "\r" not in written, "file must be one line"
    assert not written.endswith("\n"), "file must have no trailing newline"
    assert written.startswith(("feat:", "fix:", "chore:")), "must read as a commit message"
    assert "Friday" in written, "entry must carry the Friday feeling"

    print(f"Wrote {len(text)} characters to /output/entry.txt")
    print(text)


if __name__ == "__main__":
    main()
