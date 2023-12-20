import pytest
from utils.code import *


# Simple fixture
@pytest.fixture
def setup_register():
    return Register("admin", "admin", "admin@gmail.com")


@pytest.fixture
def setup_login():
    return User(Account("admin", "admin", "admin@gmail.com"))


class TestSimpleFixture:
    def test_register(self, setup_register):
        assert setup_register.register() == True

    
    def test_login(self, setup_login):
        assert setup_login.login() == True


    def test_unregister(self, setup_register):
        assert setup_register.unregister() == True
        