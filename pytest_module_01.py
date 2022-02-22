# write test case pass and fail 

def test_pass():

    assert 5 + 5 == 10
    assert 5 - 5 == 0
    assert 5 * 5 == 25
    assert 5/5  == 1


def test_fail():
    assert 9/5 == 1, "failed test"
    assert 5 - 5 == 2 , "failed test"



print(test_pass)
print(test_fail)