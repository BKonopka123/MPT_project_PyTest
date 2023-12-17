import pytest
from utils.code import *

@pytest.mark.test_login(username="admin", password="admin", email="admin@gmail.com")
class TestLogin:
    def test_login(self, setup_login):
        register, user = setup_login
        assert register.register() == True
        assert user.login() == True
        assert user.is_logged() == True
        assert user.do_something() == True

