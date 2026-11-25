"""Passive-aggressive fridge note.

The fridge keeps score: door sensors, expiry dates, and every
midnight visit. This note is what it finally prints on its screen.
"""

import os
from pathlib import Path

# One line, dry and petty: the fridge counted the door opens, mourned
# the yogurt, and demoted itself to a cold closet. The sting is the
# self-demotion — it stops nagging about the food and files itself
# under furniture the owner only visits at 2 a.m.
LINE = "Your yogurt expired Tuesday and I counted. 47 door opens today, 0 meals cooked \u2014 at this point I'm just a cold closet you visit at 2 a.m."

assert 1 <= len(LINE) <= 200, f"LINE must be 1-200 chars, got {len(LINE)}"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
