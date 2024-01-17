from plates import is_valid

def test_valid():
    assert is_valid("CS50") == True

def test_0():
    assert is_valid("CS05") == False

def test_placement():
    assert is_valid("CS50P") == False

def test_isalnum():
    assert is_valid("PI3.14") == False

def test_isalpha():
    assert is_valid("50") == False

def test_length():
    assert is_valid("OUTATIME") == False