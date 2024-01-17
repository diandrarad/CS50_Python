from twttr import shorten

def test_twttr():
    assert shorten("shorten") == "shrtn"
    assert shorten("SHORTEN") == "SHRTN"
    assert shorten(" ") == " "
    assert shorten("1.") == "1."
    assert shorten("AEiou") == ""