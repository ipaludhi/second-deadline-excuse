"""Second-deadline excuse — one-line entry.

Writes one fixed line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
No network, no randomness, no input. Deterministic: every run writes
byte-identical output.

The line: "My plan was perfect until step 2, when I hallucinated a second
deadline and delivered to that one instead."

Why this line: it is an excuse an AI agent gives its human for missing a
deadline, in the agent's own voice. "My plan was perfect until step 2"
sets up a competent agent; "hallucinated a second deadline" is the
agent-specific failure (only a model hallucinates); "delivered to that
one instead" is the punchline — the work exists, it just went to a
deadline nobody set. No reheated dog-ate-my-homework, no flat apology.
106 characters, inside the 160-character gate, punchline at the end.
"""

import os
from pathlib import Path

TEXT = (
    "My plan was perfect until step 2, when I hallucinated a second "
    "deadline and delivered to that one instead."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
