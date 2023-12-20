import pytest
from utils.code import *

@pytest.fixture
def setup_register():
    return Register("admin", "admin", "admin@gmail.com")


# Autouse argument in fixtures
@pytest.fixture(autouse=True)
def login(setup_register):
    setup_register.register()
    pytest.calls = 1


class TestAutouseArgument:
    def test_login(self):
        assert pytest.calls == 1
        user = User(Account("admin", "admin", "admin@gmail.com"))
        assert user.login() == True
