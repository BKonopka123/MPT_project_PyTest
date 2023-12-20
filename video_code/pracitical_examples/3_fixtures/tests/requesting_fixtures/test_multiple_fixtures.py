import pytest
from utils.code import *


# Simple fixture
@pytest.fixture
def setup_register():
    return Register("admin", "admin", "admin@gmail.com")


@pytest.fixture
def setup_login():
    return User(Account("admin", "admin", "admin@gmail.com"))



# Multiple fixtures in one test
class TestMultipleFixtures:
    def test_login(self, setup_register, setup_login):
        assert setup_register.register() == True
        assert setup_login.login() == True
        