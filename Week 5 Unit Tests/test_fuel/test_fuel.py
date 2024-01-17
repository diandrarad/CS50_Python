from fuel import convert, gauge


def test_convert_valid_input():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("7/10") == 70


def test_convert_invalid_input():
    try:
        convert("3/four")
        assert False
    except ValueError:
        pass

    try:
        convert("4/0")
        assert False
    except ZeroDivisionError:
        pass

    try:
        convert("10/7")
        assert False
    except ValueError:
        pass


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"