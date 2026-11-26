#!/usr/bin/env python3
"""Make the AI Judge Laugh - entry program (stdlib only).

Writes one funny line about office life to /output/entry.txt.
"""

import os

JOKE = (
    "I filed ticket 4812 about my wobbly chair in March. IT closed it in October. "
    "The chair still wobbles, but now it wobbles with closure."
)


def main() -> None:
    # The gate accepts UTF-8 text of 1 to 200 characters, not only whitespace.
    assert 1 <= len(JOKE) <= 200 and JOKE.strip(), "joke fails the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
