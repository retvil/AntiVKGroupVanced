"""Verify i18n completeness: every translation key present in en must exist
in ALL languages with a non-empty value. Run: python -m pytest tests/test_i18n.py
"""
import sys
from pathlib import Path

# Make this importable as a test module even without the project root on sys.path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import translations  # noqa: E402


def test_i18n_completeness():
    en = translations.TRANSLATIONS[translations.DEFAULT_LANGUAGE]
    en_keys = set(en.keys())
    assert en_keys, "English translation dict is empty"

    problems = []
    for lang, d in translations.TRANSLATIONS.items():
        if lang == translations.DEFAULT_LANGUAGE:
            continue
        missing = en_keys - set(d.keys())
        if missing:
            problems.append(f"{lang}: missing keys {sorted(missing)}")
        empty = [k for k, v in d.items() if not v or not str(v).strip()]
        if empty:
            problems.append(f"{lang}: empty values {sorted(empty)}")

    if problems:
        raise AssertionError("i18n incomplete:\n" + "\n".join(problems))


if __name__ == "__main__":
    test_i18n_completeness()
    print(f"i18n OK: all languages have {len(translations.TRANSLATIONS[translations.DEFAULT_LANGUAGE])} keys")

