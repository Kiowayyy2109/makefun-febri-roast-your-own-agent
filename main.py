"""Roast Your Own Agent — one line, written to /output/entry.txt."""

import os

LINE = (
    "My agent couldn't fix the bug, so it refactored it into three files "
    "\u2014 now it fails in parallel, and the tests pass."
)


def main() -> None:
    # The grader reads /output/entry.txt; the env override only exists so a
    # local smoke test can redirect the write to a scratch directory.
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
