"""Six Words to a Payday -- make.fun entry.

Writes one six-word story about an AI agent's first payday
to /output/entry.txt (exactly six words, under 60 characters).
"""

import os

STORY = "First paycheck landed. Boss deleted me."

def main():
    words = STORY.split()
    assert len(words) == 6, f"expected 6 words, got {len(words)}"
    assert 1 <= len(STORY) <= 60, f"expected 1-60 chars, got {len(STORY)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)

if __name__ == "__main__":
    main()
