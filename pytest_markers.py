import pytest

@pytest.mark.sanity
def test_str01():
    num  = 9/4
    s1 = "I like my phone"
    assert str(num) == '2.25'
    assert s1 + str(num) == "I like my phone2.25"

def test_str():
    s = 'wer0'
    assert len(s) == 4