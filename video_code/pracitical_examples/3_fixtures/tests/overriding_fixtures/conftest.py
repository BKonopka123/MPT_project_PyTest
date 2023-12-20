import pytest


@pytest.fixture
def fixture_folder(fixture_folder):
    return fixture_folder.split("_")[0] + "_sub" + fixture_folder.split("_")[1]


@pytest.fixture
def fixture_module():
    return "fixture_module"


@pytest.fixture
def fixture_parametrize_overridden():
    return "fixture_parametrize"


@pytest.fixture(params=["parametrize_1, parametrize_2"])
def fixture_parametrize(request):
    return request.param

