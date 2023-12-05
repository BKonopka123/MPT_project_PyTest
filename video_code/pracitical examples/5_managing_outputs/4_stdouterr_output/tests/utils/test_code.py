import pytest
import sys
from utils import code

#1
# def test_func1():
#     print("Example stdout 1")
#     sys.stderr.write("Example stderr 1")
#     assert True

# def test_func2():
#     print("Example stdout 2")
#     sys.stderr.write("Example stderr 2")
#     assert False

#2 - pytest
def test_myoutput(capsys): 
    print("hello")
    sys.stderr.write("world\n")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
    assert captured.err == "world\n"
    print("next")
    captured = capsys.readouterr()
    assert captured.out == "next\n"