import pytest
from pathlib import Path


class TestMonkeyPatch:
    # tmp_path is a pytest fixture that creates a temporary directory
    # for each test and deletes it afterwards. It is a pathlib.Path object.
    # For more information see: https://docs.pytest.org/en/latest/tmpdir.html
    def test_get_ssh(self, monkeypatch, tmp_path):


        def mockreturn ():
            return Path("/test")
        

        monkeypatch.setattr(Path, "home", mockreturn)
    
        dummy_ssh = tmp_path / ".dummy_ssh"
        dummy_ssh.mkdir()

        assert Path.home() / ".dummy_ssh" == Path("/test/.dummy_ssh")

