import pytest
from utils import code

class Test_fun_1:
    def test_sort(self):
        list1 = [3,2,1]
        assert code.arr_sort(list1) == [1,2,3]
    
    def test_find(self):
        list1 = [8,9,15]
        assert code.arr_find(list1, 9) == 1
    
    def test_min(self):
        list1 = [19,-5,16]
        assert code.arr_min(list1) == -5
    
    def test_max(self):
        list1 = [100,9,28]
        assert code.arr_max(list1) == 100
    
    def test_reverse(self):
        list1=[1,2,3]
        assert code.arr_reverse(list1) == [3,2,1]