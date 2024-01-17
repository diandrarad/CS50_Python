from jar import Jar
import pytest


def test_init():
    # Test capacity is a non-negative int
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("not an int")
    with pytest.raises(ValueError):
        Jar(2.5)

def test_str():
    jar = Jar(10)
    jar.deposit(3)
    assert str(jar) == 3 * "🍪"

def test_deposit():
    jar = Jar(10)
    # Test adding cookies within capacity
    jar.deposit(5)
    assert jar.size == 5

    # Test adding cookies that exceed capacity
    with pytest.raises(ValueError):
        jar.deposit(10)

    # Test adding negative number of cookies
    with pytest.raises(ValueError):
        jar.deposit(-1)

def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    # Test withdrawing cookies
    jar.withdraw(2)
    assert jar.size == 3

    # Test withdrawing more cookies than available
    with pytest.raises(ValueError):
        jar.withdraw(4)

    # Test withdrawing negative number of cookies
    with pytest.raises(ValueError):
        jar.withdraw(-1)

def test_capacity():
    jar = Jar(10)
    assert jar.capacity == 10

def test_size():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5