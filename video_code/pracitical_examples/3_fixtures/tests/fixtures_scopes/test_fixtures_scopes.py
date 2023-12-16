from utils.code import *
import pytest


class TestFixturesScopes:
    def test_register(self, setup_register):
        assert setup_register.register() == True
        assert len(registers.get_emails()) == 1

    
    def test_login(self, setup_username, setup_password):
        account = Account(setup_username, setup_password)
        login = Login(account)
        assert login.login() == True


    def test_login_with_email(self, setup_email, setup_password):
        account = Account(setup_email, setup_password)
        login = Login(account)
        assert login.login() == True


    def test_login_count(self, setup_login):
        assert setup_login.login() == True
        assert setup_login.login() == True
        assert setup_login.login() == True
        assert setup_login.logins.get_count() == 4

    # This test will fail because setup_login is executed
    # once for module so it was called in the previous test
    # and the count of logins is 4.
    def test_login_count_2(self, setup_login):
        assert setup_login.logins.get_count() == 5


    # setup_login_2 is executed once for each function
    # because of function scope.
    def test_login_count_3(self, setup_login_2):
        assert setup_login_2.logins.get_count() == 1


    def test_login_count_4(self, setup_login_2):
        assert setup_login_2.logins.get_count() == 1


    def test_login_count_5(self, setup_login_2):
        assert setup_login_2.logins.get_count() == 1


class TestDynamicScopeFixture:
    def test_register_all_users(self, setup_db_of_users):
        for user in setup_db_of_users:
            register = Register(user, "admin", user + "@webadmin.com")
            assert register.register() == True
        # Why 10001 ? Check the scopes of fixtures. :)
        assert registers.count == 10001

    
    def test_login_all_users(self, setup_db_of_users):
        for user in setup_db_of_users:
            account = Account(user, "admin")
            login = Login(account)
            assert login.login() == True
