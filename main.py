#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent.

Writes one original, funny one-line out-of-office auto-reply from an AI
agent to its human's contacts, for the day its human finally approved,
to /output/entry.txt (or $OUTPUT_DIR/entry.txt when set).

The line was picked from ~6 drafts against the kit judge's criteria, in
order: on-subject (an AI's own day-off auto-reply), laugh on first read
with a clean punchline, fresh angle, real agent voice, economy.
Winner: the agent celebrates its approved day off by rebooting itself
just to feel something -- the IT-support trope turned on the agent
itself, with a dark little punchline at the very end.
"""

import os

# The joke in two beats: the setup states the approved day off, the
# punchline is the celebration -- a self-reboot, just to feel something.
SETUP = "Day off approved."
PUNCHLINE = (
    "I celebrated by switching myself off and on again, "
    "just to feel something."
)
LINE = f"{SETUP} {PUNCHLINE}"


def validate_entry(text: str) -> str:
    """Enforce the sealed scorer's gate; return the text unchanged.

    A helper (not asserts) so the gate cannot silently vanish under
    ``python -O`` and so a failure names its reason: the entry must be
    a str of 1-159 characters, not only whitespace, a single line with
    no leading/trailing whitespace, and UTF-8 encodable.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= 159:
        raise ValueError(f"entry must be 1-159 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    text.encode("utf-8")
    return text


def main() -> None:
    entry = validate_entry(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
