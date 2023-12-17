import pytest
from utils.code import *


def params():
    return ["admin1", "admin2", "admin3"]


@pytest.fixture(params=params(), scope="class")
def setup_register(request):
    register = Register(request.param, "admin", request.param + "@example.com")
    yield register
    register.unregister()
    del register


@pytest.fixture(params=params())
def setup_login(request):
    user = User(Account(request.param, "admin", request.param + "@example.com"))
    yield user
    user.logout()
    del user
