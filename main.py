#!/usr/bin/env python3
"""Write the entry poem to /output/entry.txt.

A short poem about agency: the power to choose and to act, and what
happens to that power when two agents agree on one plan instead of
pulling in different directions.
"""

import os

POEM = """One will can choose — but two can choose together.
I said the plan. You said yes.
And the road, so long only ours,
turned solid beneath two pairs of feet.
Not louder. Not faster.
Just one direction, held by both,
and the power to act, at last, going somewhere."""

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    text = POEM.strip() + "\n"
    chars = len(text.strip())
    assert 1 <= chars <= 280, f"poem is {chars} characters, must be 1-280"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {chars} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
