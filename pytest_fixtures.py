import pytest

@pytest.fixture()
def setup_list():
    print('fixtures below')
    city = ['New York',"London"]
    return city


def test_getItem(setup_list):
    print(setup_list)
    assert setup_list[0] == "New York"
    assert setup_list[::1] == ["New York","London"]