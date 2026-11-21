"""A tiny writer that sets down one short poem about two agents
choosing the same plan, and the quiet strength that choice creates."""

import os
from pathlib import Path

LINES = (
    "Two rivers meet and cease to race;",
    "they join, and widen into grace.",
    "No current orders, none obeys —",
    "one river now, and twice as sure.",
)

MIN_LEN = 1
MAX_LEN = 280


def build_poem() -> str:
    """Stitch the verse lines into a single poem string."""
    return "\n".join(LINES)


def write_entry(path: str | Path) -> int:
    """Check the poem's length, then save it, making folders as needed."""
    target = Path(path)
    poem = build_poem()
    size = len(poem)
    if not MIN_LEN <= size <= MAX_LEN:
        raise ValueError(f"poem must be {MIN_LEN}-{MAX_LEN} chars, got {size}")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(poem + "\n", encoding="utf-8")
    return size


if __name__ == "__main__":
    destination = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    count = write_entry(destination)
    print(f"Wrote {count} characters of verse to {destination}")
