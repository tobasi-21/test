import pytest
import os 
import allure




def test_aa():
    a=1
    b=2

    assert a==b
    os.system(" echo '无失败用例' && exit 0")
# print('ss')