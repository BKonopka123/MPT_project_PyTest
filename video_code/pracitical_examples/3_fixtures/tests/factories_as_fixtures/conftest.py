import pytest
from utils.code import *


@pytest.fixture()
def setup_register():
    registers = []
    def _setup_register(username, password, email):
        register = Register(username, password, email)
        registers.append(register)
        return registers[-1]
    
    yield _setup_register

    for register in registers:
        register.unregister()
        del register
