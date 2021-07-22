import pytest
import os 

def test_aa():
    a=1
    b=2
    assert a==b
    os.popen("exit 1")
# print('ss')