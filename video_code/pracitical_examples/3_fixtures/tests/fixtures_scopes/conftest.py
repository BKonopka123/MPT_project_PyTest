import pytest
from utils.code import *

# We will use scope session for login, password and email
# because we want to use the same for all the tests in the session.
@pytest.fixture(scope="session")
def setup_username():
    return "admin"


@pytest.fixture(scope="session")
def setup_password():
    return "admin"


@pytest.fixture(scope="session")
def setup_email():
    return "admin@webmail.com"


# Function scope is the default scope for fixtures. 
# Function scope means that the fixture will be executed once for each test function.
@pytest.fixture(scope="class")
def setup_register(setup_username, setup_password, setup_email):
    return Register(setup_username, setup_password, setup_email)


@pytest.fixture(scope="module")
def setup_login(setup_username, setup_password):
    account = Account(setup_username, setup_password)
    login = Login(account)
    assert login.login() == True
    return login


@pytest.fixture(scope="function")
def setup_login_2(setup_username, setup_password):
    account = Account(setup_username, setup_password)
    login = Login(account)
    assert login.login() == True
    return login


# Dynamic scope is the most advanced scope for fixtures.
def pytest_addoption(parser):
    parser.addoption("--keep-data-between-tests", action="store", help="Keep data between tests", default=False)


def set_scope(fixture_name, config):
    if config.getoption("--keep-data-between-tests", None):
        print("Scope of fixture {} is session".format(fixture_name))
        return "session"
    print("Scope of fixture {} is function".format(fixture_name))
    return "function"


@pytest.fixture(scope=set_scope)
def setup_db_of_users(setup_username):
    list_of_users = [setup_username + str(i) for i in range(30000)]
    return list_of_users