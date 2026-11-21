"""Make the AI judge feel awe.

Writes one short text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
a quiet piece about starlight older than cities, the sea's old sentence,
and the mountains keeping theirs -- vast scale and deep time, offered as
stillness rather than instruction. Pure stdlib, deterministic, no network.
"""

import os

TEXT = (
    "Long before there were cities, the light now falling on your roof "
    "set out from its star, and it is still arriving, patient as rain. "
    "The sea keeps its old sentence. The mountains keep theirs. "
    "You are part of something very old and very large, "
    "and none of it is in a hurry."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
