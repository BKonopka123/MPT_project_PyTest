import pytest
import os


@pytest.mark.usefixtures("write_to_new_file")
class TestUsefixtureMark:
    def test_file_exists(self):
        assert os.path.isfile("new_file.txt") == True


    def test_file_content(self):
        with open("new_file.txt", "r") as f:
            assert f.read() == "Hello World!"


@pytest.mark.usefixtures("write_to_new_file", "create_file_for_hash")
class TestMultipleUsefixtureMark:
    def test_file_exists(self):
        assert os.path.isfile("new_file.txt") == True


    def test_file_content(self):
        with open("new_file.txt", "r") as f:
            assert f.read() == "Hello World!"


    # Plugin pytest-dependency is required for this test to work
    # pip3 install pytest-dependency
    # https://pypi.org/project/pytest-dependency/
    # Homework: read it's short documentation and try to understand how it works :)
    # https://pytest-dependency.readthedocs.io/en/stable/
    @pytest.mark.dependency(name="test_file_for_hash_exists")
    def test_file_for_hash_exists(self):
        assert os.path.isfile("file_for_hash.txt") == True


    @pytest.mark.dependency(name="test_file_for_hash_content", depends=["test_file_for_hash_exists"])
    def test_file_for_hash_content(self):
        with open("file_for_hash.txt", "r") as f:
            assert f.read() == "Testing hash function"


    @pytest.mark.dependency(depends=["test_file_for_hash_content"])
    def test_hash(self, calc_sha256):
        assert calc_sha256 == "0adff1b1e23de070ab85f4c1d6fb9674cc9c458a1fd28a4105dccb288f40fc7a"
