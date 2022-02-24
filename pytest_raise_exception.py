

import pytest

# use rasises to pass the exception
def test_case01():

    with pytest.raises(Exception):
        assert(1/0)


def test_case02():
    with pytest.raises(Exception) as expinf:
        assert (1,2,3) == (1,2,4) 
    print(str(expinf))