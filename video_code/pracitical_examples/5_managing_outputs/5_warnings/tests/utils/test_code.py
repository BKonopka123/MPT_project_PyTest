import pytest
import warnings
from utils import code

#pytest -q test_code.py -W error::UserWarning

#1
def test_fun1():
    assert code.fun1() == True

#2 - pytest site
def test_fun2():
    with pytest.warns() as record:
        warnings.warn("user", UserWarning)
        warnings.warn("runtime", RuntimeWarning)
    assert len(record) == 2
    assert str(record[0].message) == "user"
    assert str(record[1].message) == "runtime"

def test_fun3(recwarn):
    warnings.warn("hello", UserWarning)
    assert len(recwarn) == 1
    w = recwarn.pop(UserWarning)
    assert issubclass(w.category, UserWarning)
    assert str(w.message) == "hello"
    assert w.filename
    assert w.lineno