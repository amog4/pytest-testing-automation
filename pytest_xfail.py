import pytest

def test_join():

    s = ['world,eoie']
    assert ' '.join(s) == 'world,eoie'

@pytest.mark.xfail
def test_str():
    s = 'wer0'
    assert len(s) == 5