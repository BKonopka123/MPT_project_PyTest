import pytest
from utils.code import *


class TestTeardownUnsafe:
    def test_do_something(self, setup_user_unsafe):
        assert setup_user_unsafe.do_something() == True
      