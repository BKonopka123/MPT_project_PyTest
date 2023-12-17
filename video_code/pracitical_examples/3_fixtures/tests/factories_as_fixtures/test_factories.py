import pytest
from utils.code import *

class TestFactoryFixture:
    def test_register(self, setup_register):
        user1 = setup_register('admin1', 'admin', 'admin1@gmail.com')
        assert user1.register() == True
        user2 = setup_register('admin2', 'admin', 'admin2@gmail.com')
        assert user2.register() == True
        user3 = setup_register('admin3', 'admin', 'admin3@gmail.com')
        assert user3.register() == True
        assert registered_users.get_count() == 3