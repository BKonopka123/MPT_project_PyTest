import pytest
from utils import code

#assert keyword
def test_fun_1():
    assert code.fun_1() == 2

def test_fun_1_2():
    assert code.fun_1() == 3

def test_fun_1_3():
    assert code.fun_1() % 2 == 1, "value was even, should be odd"

def test_string():
    longstr = "asdasdasdasdasdasdasdasdasdasdasd2dadczvdvs"
    assert "2" in longstr

#raising errors
def test_fun_2():
    with pytest.raises(ZeroDivisionError):
        code.fun_2()

def test_fun_3():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        code.fun_3()

@pytest.mark.xfail(raises=ZeroDivisionError)
def test_fun_2_2():
    code.fun_2()

run_test_condition = True
@pytest.mark.skipif(condition=run_test_condition, reason="Skipping this test conditionally.")
def test_conditional_skip():
    assert False

def test_fun_4():
    pytest.raises(ZeroDivisionError, code.fun_4, 0) #nie mozna tu dac nawiasow do nazwy funkcji

#context-sensitive comparisons
def test_list_comparison():
    list1 = [1,2,3]
    list2 = [1,4,3]
    assert list1 == list2

#Defining your own explanation for failed assertions
class Foo:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val

def test_compare():
    f1 = Foo(1)
    f2 = Foo(2)
    assert f1 == f2


