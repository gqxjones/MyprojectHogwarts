#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
pytest的基本使用
'''

import pytest
import yaml
from python.Calc import Calc

@pytest.fixture(scope="module", params=[
    [1,1,2],
    [2,1,3]
])

def data(request):
    yield request.param

class TestFixture:

    def setup(self):
        print("setup")
        self.Calc = Calc()

    def test_add(self):
        assert 1 + 1 == 2

    def test_add2(self, data):
        assert data[0] + data[1] == data[2]

    with open("./test_pytest.yaml") as f:

        data2 = yaml.load(f)
    @pytest.mark.parametrize('result, a, b', data2)
    def test_add3(self, result, a, b):
        assert self.Calc.add(a, b) == result