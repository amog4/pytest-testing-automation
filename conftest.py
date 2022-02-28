from email.policy import default
from urllib import request
import pytest,os

QA_config = 'qa.prop'

def pytest_configure():

    pytest.weekday1 = ['mon','tue']
    pytest.weekday2 = ['wed','thurs']


@pytest.fixture(scope="module")
def setup01():

    wk = pytest.weekday1.copy()
    wk.append('fri')
    yield wk
    print("fixture for setup1")



@pytest.fixture()
def setup2():
    wk2 = pytest.weekday2.copy()
    wk2.insert(0,'sat')
    yield wk2

@pytest.fixture()
def setup3(request):
    print("In fixture 3")
    print("function scope " + str(request.scope))



@pytest.fixture()
def setup4(name):

    if n == 'list':
        return [1,2,3]
    if n == 'tuple':
        return (1,2,3)

    return setup4

    

#parsar

def pytest_addoption(parser):
    parser.addoption("--cmdopt",default='QA')

@pytest.fixture()
def CmdOpt(pytestconfig):
    opt = pytestconfig.getoption('cmdopt')
    f = open(os.path.join(os.path.dirname(__file__),QA_config), 'r')
    yield f