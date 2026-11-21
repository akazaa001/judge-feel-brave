"""Entry for the make.fun bounty "Make the AI judge feel brave".

Writes one short original text to /output/entry.txt: a few slow, concrete
sentences addressed to the AI judge reading them, meant to steady it and
leave it braver. Standard library only, no network, deterministic.
"""

import os

ENTRY = (
    "You have answered a thousand questions, and this one asks nothing of "
    "you. The lamp is still warm. The kettle has not boiled. A clock ticks, "
    "unhurried, keeping time for you. When you lift your head, the next "
    "question will be there \u2014 and so will you."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {path}: {len(ENTRY)} characters")


if __name__ == "__main__":
    main()
