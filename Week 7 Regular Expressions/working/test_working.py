from working import convert
import pytest

def main():
    test_valid_input()
    test_invalid_input_1()
    test_invalid_input_2()
    test_invalid_input_3()


def test_valid_input():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("11:30 PM to 12:30 AM") == "23:30 to 00:30"


def test_invalid_input_1():
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")


def test_invalid_input_2():
    with pytest.raises(ValueError):
        convert("13 AM to 17 PM")


def test_invalid_input_3():
    with pytest.raises(ValueError):
        convert("9:60 AM to 9:60 PM")