from um import count

def main():
    test_0()
    test_1()
    test_2()


def test_0():
    assert count("yum") == 0
    assert count("yummy") == 0


def test_1():
    assert count("um...") == 1
    assert count("hello, um, world") == 1


def test_2():
    assert count("um, hello, um, world") == 2
    assert count("Um, thanks, um...") == 2