"""Deadpan forecast for Blundervost, a city that does not exist.

Writes exactly one forecast line (148 characters, under the 160 cap)
to /output/entry.txt. Deterministic: the same line on every run.
"""

from pathlib import Path

ENTRY = (
    "In Blundervost, expect 41 degrees and a light rain of lost umbrellas, "
    "with 60-kilometre-an-hour gusts chasing hats down Market Street until Tuesday."
)


assert 1 <= len(ENTRY) <= 160, "forecast line must be 1-160 characters"
assert "\n" not in ENTRY, "forecast line must be a single line"


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
