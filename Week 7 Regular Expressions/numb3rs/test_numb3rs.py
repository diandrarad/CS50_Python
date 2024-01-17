from numb3rs import validate

def main():
    test_valid()
    test_invalid()

def test_valid():
    assert validate("127.0.0.1") == True
    assert validate("192.168.1.1") == True
    assert validate("10.0.0.1") == True
    assert validate("172.16.0.1") == True
    assert validate("255.255.255.255") == True

def test_invalid():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("300.168.1.1") == False
    assert validate("192.168.1") == False
    assert validate("hello.world") == False