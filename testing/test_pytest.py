#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
pytest的基本使用
'''

import pytest
from python.Calc import Calc


class TestCalc:

    def setup(self):
        print("setup")
        self.Calc = Calc()

    @pytest.mark.parametrize('result, a, b', [
        [2, 0, 2],
        [3, 1, 2],
        [0, 2, 2],
        [-2, -3, -5],
        [1, 3, 4]
    ])
    #加法
    # @pytest.mark.run(order=-1)
    def test_zaddOne(self, result, a, b):
        # assert self.Calc.add(0, 2) == 2
        assert self.Calc.add(a, b) == result

    # @pytest.mark.run(order=1)
    # def test_addTwo(self):
    #     assert self.Calc.add(1, 2) == 3

    @pytest.mark.parametrize('divResult, c, d', [
        [0.5, 1, 2],
        [2, 2, 1],
        [2, 0.2, 0.1]
    ])
    #除法
    def test_divOne(self, divResult, c, d):
        assert self.Calc.div(c, d) == divResult

    def test_divTwo(self):
        with pytest.raises(ZeroDivisionError):
            self.Calc.div(2, 0)
