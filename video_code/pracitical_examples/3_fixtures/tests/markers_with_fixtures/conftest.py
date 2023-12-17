import pytest
from utils.code import *


@pytest.fixture
def setup_login(request):
    username = request.node.get_closest_marker("test_login").kwargs.get("username")
    password = request.node.get_closest_marker("test_login").kwargs.get("password")
    email = request.node.get_closest_marker("test_login").kwargs.get("email")
    account = Account(username, password, email)
    register = Register(username, password, email)
    user = User(account)
    yield register, user
    user.logout()
    register.unregister()
    del user
    del register
    del account