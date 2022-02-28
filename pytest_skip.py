
from pyexpat import version_info
import pytest

import pytest,sys

@pytest.mark.skip(reason='skip')
def test_a1():
    assert 4 != 3


@pytest.mark.skipif(sys.version_info > (3,8),reason='skip')
def test_a1():
    assert 4 != 3

