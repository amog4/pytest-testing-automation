from calendar import c
import pytest
import math

data = [([2,3,4],'sum',9),([2,3,4],'prod',24)]

@pytest.mark.parametrize("a,b,c",data)
def test_param(a,b,c):
    if b == 'sum':
        assert sum(a) == c
    if b == 'prod':
        assert math.prod(a) == c

