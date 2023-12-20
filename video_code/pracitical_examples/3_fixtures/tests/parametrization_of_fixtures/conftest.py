import pytest
from utils.code import *


@pytest.fixture(params=["admin1", "admin2", "admin3"])
def setup_register(request):
    register = Register(request.param, "admin", request.param + "@gmail.com")
    yield register
    register.unregister()
    del register


def get_param(fixture_value):
    return ["admin1", "admin2", "admin3"][fixture_value] if fixture_value < 3 else None


@pytest.fixture(params=[0, 1, 2], ids=get_param)
def setup_register_2(request):
    register = Register(get_param(request.param), "admin", get_param(request.param) + "@gmail.com")
    yield register
    register.unregister()
    del register


@pytest.fixture(params=["admin1", pytest.param("admin2", marks=pytest.mark.skip),
                        pytest.param("admin3", marks=pytest.mark.admin3)])
def setup_register_3(request):
    register = Register(request.param, "admin", request.param + "@gmail.com")
    yield register
    register.unregister()
    del register