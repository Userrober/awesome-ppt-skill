#!/usr/bin/env python3
"""WCAG contrast ratio between two hex colors.

Usage: contrast.py <fg> <bg> [--json]
Examples:
  contrast.py F2F4F8 1E2761     -> ratio + pass/fail verdicts
  contrast.py '#333' '#fff' --json
Exit code 0 if body-text pass (>= 4.5:1), 1 otherwise.
"""

import json
import sys


def _channel(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hex_str: str) -> float:
    s = hex_str.strip().lstrip("#")
    if len(s) == 3:
        s = "".join(ch * 2 for ch in s)
    if len(s) == 8:  # drop alpha if someone pastes an ARGB hex
        s = s[2:] if len(s) == 8 else s
    if len(s) != 6:
        raise ValueError(f"bad hex color: {hex_str!r}")
    r, g, b = (int(s[i : i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _channel(r) + 0.7152 * _channel(g) + 0.0722 * _channel(b)


def contrast_ratio(fg: str, bg: str) -> float:
    l1, l2 = luminance(fg), luminance(bg)
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    as_json = "--json" in argv
    if len(args) != 2:
        print(__doc__)
        return 2
    ratio = contrast_ratio(*args)
    body_ok = ratio >= 4.5
    large_ok = ratio >= 3.0
    if as_json:
        print(json.dumps({
            "fg": args[0].lstrip("#"), "bg": args[1].lstrip("#"),
            "ratio": round(ratio, 2),
            "body_text": body_ok, "large_text": large_ok,
        }))
    else:
        verdict = "PASS body & large" if body_ok else ("large text only" if large_ok else "FAIL")
        print(f"{ratio:.2f}:1  {verdict}")
    return 0 if body_ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
