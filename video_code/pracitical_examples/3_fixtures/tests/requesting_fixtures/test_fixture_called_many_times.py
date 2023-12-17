import pytest
from utils.code import *

# Fixture mistakenly requesting another fixture which
# was already called.
@pytest.fixture
def setup_username():
    return "admin"


@pytest.fixture
def setup_password():
    return "admin"


@pytest.fixture
def setup_email():
    return "admin@gmail.com"


@pytest.fixture
def setup_register(setup_username, setup_password, setup_email):
    return Register(setup_username, setup_password, setup_email)


@pytest.fixture
def setup_account(setup_username, setup_password, setup_email):
    return Account(setup_username, setup_password, setup_email)


@pytest.fixture
def setup_login(setup_account):
    user = User(setup_account)
    assert user.login() == True
    return user


@pytest.fixture
def try_another_login(setup_login):
    pass


class TestFixtureRequestingAnotherFixtureWithMistake:
    def test_register(self, setup_register):
        assert setup_register.register() == True


    def test_login(self, setup_login, try_another_login):
        # This test failes because user logged in already
        # in setup_login fixture and we are trying to login
        # again in this test.
        # As you can see in try_another_login fixture there
        # is no code it is just to check whether setup_login
        # fixture is called again or not.
        # If it has been called again then it would have return
        # False and there will be raised an error in this fixture.
        assert setup_login.login() == True
