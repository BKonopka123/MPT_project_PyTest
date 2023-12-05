import pytest
from utils import code
import pdb; pdb.set_trace()

#pytest -x test_code.py
#pytest --maxfail=2 test_code.py
#pytest --pdb test_code.py
#pytest -x --pdb test_code.py
#pytest --pdb --maxfail=3 test_code.py
#pytest --trace test_code.py

def test_fun_1():
    assert code.fun() == 2

def test_fun_2():
    breakpoint()
    assert code.fun() == 3

def test_fun_3():
    assert code.fun() == 4   