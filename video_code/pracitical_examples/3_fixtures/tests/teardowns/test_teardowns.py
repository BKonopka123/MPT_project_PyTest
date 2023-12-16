import pytest
from utils.code import *


class TestTeardownUnsafe:
    def test_do_something(self, setup_user_action):
        assert setup_user_action.do_something() == True


class TestTeardownSafe:
    def test_register(self, setup_register):
        assert setup_register.register() == True


    def test_login(self, setup_login):
        assert setup_login.login() == True


    def test_do_something_safe(self, setup_user_action_safe):
        assert setup_user_action_safe.do_something() == True
        