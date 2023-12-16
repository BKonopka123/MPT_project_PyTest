import pytest
from utils import code


# Simple fixture
@pytest.fixture
def setup():
    return code.Account('admin', 'admin')


class TestSimpleFixture:
    def test_login(self, setup):
        login = code.Login(setup)
        assert login.login() == True


# Without fixture test can start with wrong hardcoded values
# or even start with empty ones and it will cost us time
# to find out why test is failing.
# This is not good practice !
class TestWithoutFixture:
    def test_login_2(self):
        account = code.Account('mistakeInUsername', 'admin')
        login = code.Login(account)
        assert login.login() == True


# Multiple fixtures in one test
@pytest.fixture
def setup_username():
    return "admin"


@pytest.fixture
def setup_password():
    return "admin"


class TestMultipleFixtures:
    def test_login_3(self, setup_username, setup_password):
        account = code.Account(setup_username, setup_password)
        login = code.Login(account)
        assert login.login() == True


# Fixture requesting another fixture
@pytest.fixture
def setup_username():
    return "admin"


@pytest.fixture
def setup_password():
    return "admin"


@pytest.fixture
def setup_account(setup_username, setup_password):
    return code.Account(setup_username, setup_password)


class TestFixtureRequestingAnotherFixture:
    def test_login_4(self, setup_account):
        login = code.Login(setup_account)
        assert login.login() == True


# Fixture mistakenly requesting another fixture which
# was already called.
@pytest.fixture
def setup_username():
    return "admin"


@pytest.fixture
def setup_password():
    return "admin"


@pytest.fixture
def setup_account(setup_username, setup_password):
    return code.Account(setup_username, setup_password)
 

@pytest.fixture
def login(setup_account):
    login = code.Login(setup_account)
    login.login()
    return login


# Returning value of logins to
# check if fixture was called another time
# based on logins count.
@pytest.fixture
def try_another_login(login):
    return login.logins.get_count()


class TestFixtureRequestingAnotherFixtureWithMistake:
    def test_login_5(self, login, try_another_login):
        assert login is not None
        # If fixture login has been called another time, 
        # then try_another_login should have returned 2
        # but it did not because fixture login was called only once and was cached.
        # So Pytest takes care of developers mistakes :)
        assert try_another_login == 1
        

# Fixture assure us that every test will start with the same values.
class TestFixtureAssurance:
    def test_login_6(self, setup_account):
        login = code.Login(setup_account)
        for _ in range(10):
            assert login.login() == True
        assert login.logins.get_count() == 10


    def test_login_7(self, setup_account):
        login = code.Login(setup_account)
        assert login.login() == True
        assert login.logins.get_count() == 1


    def test_login_8(self, login):
        assert login.logins.get_count() == 1


# Autouse argument in fixtures
@pytest.fixture(autouse=True)
def login(setup_account):
    login = code.Login(setup_account)
    login.login()
    # We can also use pytest_coll to collect data from fixtures
    # Of course we can use global variables but this is not good practice
    # because we can have many fixtures and we can lose track of them.
    # Moreover we could have just not use autouse argument and use fixture
    # in not autouse mode and then provide it as argument but this is just
    # for presentation of autouse argument and to give You insight how to
    # collect data from fixtures in different ways.
    pytest.logins = login.logins.get_count()
    return login

class TestAutouseArgument:
    def test_login_9(self):
        assert pytest.logins == 1