

class TestAssert():

    def test_type(self):
        assert type(1) == int
        assert type(1.3) == int

    def test_str(self):
        assert str.upper('name') == "NAME"

    


