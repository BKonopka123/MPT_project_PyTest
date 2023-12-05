import pytest
import logging
from utils import code

logging.basicConfig(level=logging.WARNING)

def test_1():
    logging.warning("Example warning log message.")
    assert 1 + 1 == 3