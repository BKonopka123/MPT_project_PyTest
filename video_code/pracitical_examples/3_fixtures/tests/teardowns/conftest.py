import pytest
from utils.code import *


# Unsafe and very unreadable fixture with teardown,
# hard to maintain, debug or extend
@pytest.fixture()
def setup_user_unsafe():
    username = "admin"
    password = "admin"
    email = "admin@gmail.com"
    account = Account(username, password, email)
    register = Register(username, password, email)
    user = User(account)
    register.register()
    user.login()
    yield user
    user.logout()
    register.unregister()
    del user
    del register
    del account


# Safe and readable fixtures but more code
# Any acctions are reduced to atomic or close to atomic operations
@pytest.fixture(scope="class")
def setup_username():
    return "admin"


@pytest.fixture(scope="class")
def setup_password():
    return "admin"


@pytest.fixture(scope="class")
def setup_email():
    return "admin@gmail.com"


@pytest.fixture(scope="class")
def setup_account(setup_username, setup_password, setup_email):
    account = Account(setup_username, setup_password, setup_email)
    yield account
    del account


@pytest.fixture(scope="class")
def setup_register(setup_username, setup_password, setup_email):
    register = Register(setup_username, setup_password, setup_email)
    yield register
    register.unregister()
    del register


@pytest.fixture(scope="class")
def setup_login(setup_account, setup_register):
    user = User(setup_account)
    yield user
    user.logout()
    del user


@pytest.fixture(scope="class")
def setup_user(setup_login):
    return setup_login
