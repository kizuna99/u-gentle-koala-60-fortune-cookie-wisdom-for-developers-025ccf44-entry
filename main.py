#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes the winning fortune-cookie line to /output/entry.txt.
The line was picked from 18 candidates by a criteria-ordered tournament
(judge criteria in order: genuine fortune wisdom for a developer, fortune-cookie
form in one breath, a true developer-day detail, a fresh turn, a quiet twist)
and refined over 6 measured iterations: a log line dashed off in anger at
3 a.m. becomes, one day, the lantern that leads a stranger out of an outage —
the throwaway line is the one that saves a stranger, which is the twist.
"""
import os

FORTUNE = (
    "An old log line, written in anger at 3 a.m., will one day be the lantern "
    "that leads a stranger out of an outage."
)


def main() -> None:
    # Gate self-check: scorer accepts UTF-8 text of 1-120 characters,
    # not only whitespace, on a single line. Fail loudly rather than
    # write an entry that can never be judged.
    assert 1 <= len(FORTUNE) <= 120, len(FORTUNE)
    assert FORTUNE.strip() == FORTUNE and "\n" not in FORTUNE
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
