#!/usr/bin/env python3
"""One Emoji, One Smile — writes exactly one emoji to /output/entry.txt.

The emoji: the face holding back tears — wholesome warmth with a
lump in the throat, the "I'm not crying, you're crying" smile.
Against a plain grin it wins on feeling, not just on cheer.
"""
import os

EMOJI = "🥹"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI + "\n")

if __name__ == "__main__":
    main()
