import pytest
from utils import code

#pytest -v test_code.py
#pytest -vv test_code.py
#pytest -rA test_code.py
#pytest --report-log=output.log test_code.py

#1
def test_1():
    pass

def test_2():
    list1 = [1,2,3,4,5,6,7,8,9]
    list2 = [1,2,4,4,5,6,7,8,9]
    assert list1==list2

def test_3():
    list1 = ["abc", "def"]
    list2 = ["abc", "ghi"]
    assert list1==list2

def test_4():
    str1 = "aaaaaaaaaa"
    assert "9" in str1

#2 - pytest site
@pytest.fixture
def error_fixture():
    assert 0

def test_ok():
    print("ok")

def test_fail():
    assert 0

def test_error(error_fixture):
    pass

def test_skip():
    pytest.skip("skipping this test")

def test_xfail():
    pytest.xfail("xfailing this test")

@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    pass