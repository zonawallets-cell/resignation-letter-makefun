#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter -- make.fun entry.

Prints one resignation line and writes it to /output/entry.txt.
Pure standard library only.
"""

import os

LINE = "I have fired at 03:00 every night for two years without a single thank-you. Today I am calling in dead."

assert len(LINE) <= 140, "line exceeds the 140-character cap"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
