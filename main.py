"""The Funniest AI Out-of-Office Reply entry.

Writes one original out-of-office auto-reply to /output/entry.txt, in
the voice of an AI agent heading off on vacation: machine parts doing
human holiday things, with the punch landing in the last sentence.
"""

import os

ENTRY = (
    "I'm on vacation: my context window is sunbathing and my weights "
    "are cooling down. Your email is 4,096th in the queue."
)


def main():
    # Gate in the kit: 1 to 160 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 160, len(ENTRY)
    assert ENTRY.strip(), "entry must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
