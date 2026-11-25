#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — writes one line to /output/entry.txt.

The line is fortune-cookie wisdom for a software developer, in one short
balanced sentence. The truth it carries: every developer has cursed legacy
code, but that code is also the record of every deadline the team actually
survived — the mess is the proof of the shipping. The twist is the second
reading: the diary is not an insult, it is a compliment to the people who
kept the thing alive.

Craft note on the revision: the first draft said the same thing with a
flatter verb ("is a diary of"), and the fortune-cookie voice was missing —
it read like an observation, not a fortune. The revision keeps the diary
image but sharpens the turn: "not a mess" sets up the expectation, the
semicolon holds the breath, and "every deadline you survived" lands as
the payoff a fortune cookie owes its reader.
"""

import os

# A fortune cookie speaks to "you" and lands in one breath: setup,
# semicolon, payoff. The line below is the whole entry.
LINE = "Your legacy code is not a mess; it is a diary of every deadline you survived."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
