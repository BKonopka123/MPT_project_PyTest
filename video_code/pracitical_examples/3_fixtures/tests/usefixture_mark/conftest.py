import pytest
import os
import tempfile
import hashlib

@pytest.fixture
def open_new_dir():
    with tempfile.TemporaryDirectory() as tmpdirname:
        old_dir = os.getcwd()
        os.chdir(tmpdirname)
        yield
        os.chdir(old_dir)



@pytest.fixture
def write_to_new_file(open_new_dir):
    with open("new_file.txt", "w") as f:
        f.write("Hello World!")
    yield
    os.remove("new_file.txt")


@pytest.fixture
def create_file_for_hash():
    with open("file_for_hash.txt", "w") as f:
        f.write("Testing hash function")
    yield
    os.remove("file_for_hash.txt")


@pytest.fixture()
def calc_sha256():
    with open("file_for_hash.txt", "rb") as f:
        bytes = f.read()
        hash = hashlib.sha256(bytes).hexdigest()
    yield hash
