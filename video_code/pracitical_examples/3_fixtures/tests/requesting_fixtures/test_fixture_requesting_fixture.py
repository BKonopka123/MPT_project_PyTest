import pytest
from utils.code import *


# Fixture requesting another fixture
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
    return User(setup_account)


class TestFixtureRequestingAnotherFixture:
    def test_register(self, setup_register):
        assert setup_register.register() == True


    def test_login(self, setup_login):
        assert setup_login.login() == True
        