import pytest
from utils.code import *


@pytest.fixture
def setup_register():
    return Register("admin", "admin", "admin@gmail.com")


@pytest.fixture
def setup_register_clean(setup_register):
    for user in registered_users.get_accounts():
        registered_users.remove_account(user)
    return setup_register


# Fixture assure us that every test will start with the same values.
class TestFixtureAssurance:
    # As you can see test_register_1-3 fail because we are trying to register
    # user with the same username, password and email which is not
    # permitted in our application.
    def test_register_1(self, setup_register):
        for _ in range(10):
            assert setup_register.register() == True


    def test_register_2(self, setup_register):
        assert setup_register.register() == True


    def test_register_3(self, setup_register):
        assert setup_register.register() == True


    def test_register_4(self, setup_register_clean):
        assert setup_register_clean.register() == True

    
    def test_register_5(self, setup_register_clean):
        assert setup_register_clean.register() == True
    
        