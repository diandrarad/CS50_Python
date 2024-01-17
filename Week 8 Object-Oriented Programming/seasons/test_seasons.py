from datetime import date
from seasons import age_in_minutes, age_in_words

def main():
    test_age_in_minutes()
    test_age_in_words()

def test_age_in_minutes():
    assert age_in_minutes(date.fromisoformat("1999-01-01")) == 12797280
    assert age_in_minutes(date.fromisoformat("1999-12-31")) == 12273120

def test_age_in_words():
    assert age_in_words(12797280) == "Twelve million, seven hundred ninety-seven thousand, two hundred eighty minutes"
    assert age_in_words(12273120) == "Twelve million, two hundred seventy-three thousand, one hundred twenty minutes"
