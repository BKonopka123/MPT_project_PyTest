import pytest
from utils.code import *

class TestParametrizationOfFixtures:
    def test_register(self, setup_register):
        assert setup_register.register() == True


    def test_register_2(self, setup_register_2):
        assert setup_register_2.register() == True


    def test_register_3(self, setup_register_3):
        assert setup_register_3.register() == True


