import pytest


def test_overriding(fixture_folder):
    print("")
    print(fixture_folder)
    pass


@pytest.fixture
def fixture_module(fixture_module):
    return fixture_module + "_overridden"


def test_overriding_module(fixture_module):
    print("")
    print(fixture_module)
    pass


@pytest.mark.parametrize("fixture_parametrize_overridden", ["directly_overriden"])
def test_overriding_parametrize(fixture_parametrize_overridden):
    print("")
    print(fixture_parametrize_overridden)
    pass


@pytest.mark.parametrize("fixture_parametrize_overridden", ["directly_overriden_2"])
def test_overriding_parametrize_2(fixture_parametrize_overridden):
    print("")
    print(fixture_parametrize_overridden)
    pass


@pytest.fixture(params=["with_parametrize_1", 
                        "with_parametrize_2"])
def fixture_module(request, fixture_module):
    return fixture_module + "_" + request.param  + "_overridden"


@pytest.fixture
def fixture_parametrize(fixture_parametrize):
    return fixture_parametrize + "_overridden"


def test_overriding_module_parametrize_vice_versa(fixture_module):
    print("")
    print(fixture_module)
    pass


def test_overriding_parametrize_vice_versa(fixture_parametrize):
    print("")
    print(fixture_parametrize)
    pass


# For more about overriding fixtures lookup for overriding fixtures from other 
# projects using pytest_plugins in conftest.py