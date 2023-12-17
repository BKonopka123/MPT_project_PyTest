from utils.code import *
import pytest


class TestDynamicScopeFixture:
    def test_register_all_users(self, setup_register_all_users):
        for user in setup_register_all_users:
            assert user.register() == True
        assert registered_users.get_count() == 30000

    
    def test_login_all_users(self, setup_login_all_users):
        for user in setup_login_all_users:
            assert user.login() == True
            assert user.is_logged() == True
