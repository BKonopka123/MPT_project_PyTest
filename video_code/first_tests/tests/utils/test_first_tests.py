import pytest


def test_1():
    pass


class TestClass:
    def test_2(self):
        pass

    def test_3(self):
        pass


@pytest.mark.my_mark
def test_4():
    pass


@pytest.mark.my_mark
class TestClass2:
    def test_5(self):
        pass

    def test_6(self):
        pass
    