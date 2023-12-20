import pytest

#simple class parametrization - all tests in class will be parametrized with the same values

@pytest.mark.skip()
@pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])
def test_simple_case(n, expected):
    assert n + 1 == expected

@pytest.mark.skip()
@pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])
class TestClass:
    @pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])
    def test_simple_case(n, expected):
        assert n + 1 == expected

    def test_weird_simple_case(self, n, expected):
        assert (n * 1) + 1 == expected

# #global parametrization - all tests in module will be parametrized with the same values

pytestmark = pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])

#marking certain parameters within the parametrization with mark.xfail

@pytest.mark.skip()
@pytest.mark.parametrize(
    "test_input,expected", [("3+5", 8), pytest.param("6*9", 42, marks=pytest.mark.xfail), ("2+4", 6)],
)
def test_eval(test_input, expected):
    assert eval(test_input) == expected

# #adding your own options to parametrization

@pytest.mark.skip()
def test_valid_string(stringinput):
    assert stringinput.isalpha()

@pytest.mark.skip()
def test_compute(param1):
    assert param1 < 4

#example of running it int he terminal pytest -q --till=4 --stringinput="hello" --stringinput="world" test_code.py