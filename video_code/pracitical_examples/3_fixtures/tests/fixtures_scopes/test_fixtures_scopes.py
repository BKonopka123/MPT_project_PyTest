from utils.code import *
import pytest


class TestFixturesScopes:
    def test_register(self, setup_register):
        assert setup_register.register() == True
        assert registered_users.get_count() == 1


    def test_login(self, setup_login):
        assert setup_login.login() == True
        assert setup_login.is_logged() == True


    def test_login_another_time(self, setup_login):
        # Because we are working on same object thanks
        # to scope class, the user is already logged in
        # after the previous test so this test will fail
        # trying to login again.
        assert setup_login.login() == True
        assert setup_login.is_logged() == True


    def test_logout(self, setup_login):
        assert setup_login.logout() == True
        assert setup_login.is_logged() == False


    def test_login_2(self, setup_login_2):
        assert setup_login_2.login() == True
        assert setup_login_2.is_logged() == True


    def test_logout_2(self, setup_login_2):
        # Because we are working on different objects thanks
        # to scope function, the user is not logged in
        # because new object is created for each test.
        assert setup_login_2.logout() == True
        assert setup_login_2.is_logged() == False
