import pytest
from utils import example


def test_fun2():
    example.fun2([1,2,3], (1,3,5), [3,2,1]) == [1,3] 