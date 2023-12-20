import pytest
from utils.code import *


class TestTeardownSafe:
    def test_register(self, setup_register):
        assert setup_register.register() == True


    def test_login(self, setup_login):
        assert setup_login.login() == True


    def test_do_something_safe(self, setup_user):
        assert setup_user.do_something() == True
