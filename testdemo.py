import pytest
import pandas as pd

def test_ver():
    assert pd.__version__ == '2.2.2'
