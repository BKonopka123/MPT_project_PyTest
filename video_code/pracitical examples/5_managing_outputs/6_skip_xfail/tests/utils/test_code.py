import pytest
sys = pytest.importorskip("sys")
from utils import code

#1
@pytest.mark.skip(reason="Skipping test")
def test_1():
    assert True

def test_2():
    a = 1
    if a != 2:
        pytest.skip("unsupported configuration")
    assert True

@pytest.mark.skipif(sys.version_info < (3, 10), reason="requires python3.10 or higher")
def test_3():
    assert True

#2
@pytest.mark.xfail
def test_4():
    assert True

def test_5():
    a = 1
    if a != 2:
        pytest.xfail("failing configuration")
    assert True

@pytest.mark.xfail(sys.platform == "win32", reason="Do not work on windows")
def test_function():
    assert True

@pytest.mark.xfail(raises=RuntimeError)
def test_function():
    assert True

@pytest.mark.xfail(run=False)
def test_function():
    assert True

@pytest.mark.xfail(strict=True)
def test_function():
    assert True