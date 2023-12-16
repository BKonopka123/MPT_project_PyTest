import pytest
from utils.code import *


# Unsafe and very unreadable fixture with teardown of all objects
@pytest.fixture()
def setup_user_action():
    register = Register("admin", "admin", "admin@gmail.com")
    register.register()
    account = Account("admin", "admin")
    login = Login(account)
    login.login()
    user = User(account)
    yield user
    user = None
    login.logins.logout()
    login = None
    register.unregister()
    register = None
    account = None


# Safe and readable fixtures but more code
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
def setup_account(setup_username, setup_password):
    account = Account(setup_username, setup_password)
    yield account
    account = None


@pytest.fixture(scope="class")
def setup_register(setup_username, setup_password, setup_email):
    register = Register(setup_username, setup_password, setup_email)
    yield register
    register.unregister()
    register = None


@pytest.fixture(scope="class")
def setup_login(setup_account, setup_register):
    login = Login(setup_account)
    yield login
    login.logins.logout()
    login = None


@pytest.fixture(scope="class")
def setup_user(setup_login):
    user = User(setup_login.account)
    yield user
    user = None


@pytest.fixture(scope="class")
def setup_user_action_safe(setup_user):
    return setup_user
