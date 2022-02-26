from calendar import weekday
from fileinput import filename
import pytest
import os

weekday1 = ['Monday','Tuesday']
weekday2 = ['Wednesday','Thursday']
filename = 'fixture_test.txt'
@pytest.fixture()
def get_list():

    weekday1.append('Friday')
    yield weekday1

    print('remove the inserted element')
    weekday1.pop()


def test_list(get_list):
    weekday2.extend(weekday1)

    assert weekday2 == ['Wednesday','Thursday','Monday','Tuesday','Friday']


# create a file 
@pytest.fixture()
def setup():

    s = open(filename  ,'w')
    s.write('testing')
    s.close()
    f = open(filename,'r+')
    yield f
    f.close()
    os.remove(filename)


def test_file(setup):

    assert setup.readline() == 'testing'