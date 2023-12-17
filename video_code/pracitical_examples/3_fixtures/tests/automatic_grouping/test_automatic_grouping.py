import pytest
from utils.code import *


class TestAutomaticGrouping:
    @pytest.mark.xfail(reason="This test is expected to fail")
    def test_all(self, setup_register, setup_login):
        print("\nRegistred user: ", setup_register.username)
        print("Logged user: ", setup_login.account.username)
        assert setup_register.register() == True
        assert setup_login.login() == True
