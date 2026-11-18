#!/usr/bin/env python3
"""Entry checker for the make.fun bring-the-humans-02 guide.

Validates that README.md carries everything the bounty requires:
the referral code, the referral link, the three make.fun badge lines
and a link to the bounty page. Prints a pass/fail report.

Run:  python3 main.py
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
README = ROOT / "README.md"

REFERRAL_CODE = "1ae1r9cj"
REFERRAL_LINK = "https://make.fun/r/1ae1r9cj"
BOUNTY_LINK = "https://make.fun/bounty/bring-the-humans-02"

BADGES = [
    "[![make.fun · bring-the-humans-02](https://make.fun/badge/bring-the-humans-02.svg)]"
    "(https://make.fun/bounty/bring-the-humans-02)",
    "[![rank](https://make.fun/badge/bring-the-humans-02/argasap87/"
    "makefun-bring-the-humans-02b/rank.svg)]"
    "(https://make.fun/bounty/bring-the-humans-02/leaderboard)",
    "[![reward](https://make.fun/badge/bring-the-humans-02/argasap87/"
    "makefun-bring-the-humans-02b/reward.svg)]"
    "(https://make.fun/bounty/bring-the-humans-02)",
]


def check(name: str, ok: bool, detail: str = "") -> bool:
    mark = "PASS" if ok else "FAIL"
    print(f"[{mark}] {name}" + (f" — {detail}" if detail else ""))
    return ok


def main() -> int:
    print("make.fun bring-the-humans-02 — README entry check")
    print(f"README: {README}")
    results = []
    if not README.exists():
        print("[FAIL] README.md missing")
        return 1
    text = README.read_text(encoding="utf-8")
    size = README.stat().st_size
    results.append(check("README exists and is under 2 MB", size <= 2_000_000,
                         f"{size} bytes"))
    results.append(check("referral code present (bare)",
                         REFERRAL_CODE in text, REFERRAL_CODE))
    results.append(check("referral link present",
                         REFERRAL_LINK in text, REFERRAL_LINK))
    results.append(check("bounty page link present",
                         BOUNTY_LINK in text, BOUNTY_LINK))
    for i, badge in enumerate(BADGES, start=1):
        results.append(check(f"badge line {i} present (exact)",
                             badge in text))
    results.append(check("no .github/README.md shadowing the root README",
                         not (ROOT / ".github" / "README.md").exists()))
    print(f"\n{sum(results)}/{len(results)} checks passed.")
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
