import pytest

def test_delItem(setup01):
    del setup01[-1]
    print(setup01)
    assert setup01 == pytest.weekday1

def test_removeItem(setup2):
    print(setup2)
    setup2.remove('thurs')
    assert setup2 == pytest.weekday2

def test_request(setup3):

    assert 1 == 1


def test_fact_fixture(setup4):
    assert type(setup4('list')) == list
    assert type(setup4('tuple')) == tuple