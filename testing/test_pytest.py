#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
pytest的基本使用
'''

import pytest
import yaml

from python.Calc import Calc


class TestCalc:

    with open("./test_pytest.yaml") as f:
        data = yaml.load(f)
    with open("./test_pytest_step.yaml") as f:
        step = yaml.load(f)

    def setup(self):
        print("setup")
        self.Calc = Calc()

    @pytest.mark.parametrize('result, a, b', data)
    #加法
    # @pytest.mark.run(order=-1)
    def test_addOne(self, result, a, b):
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

    def steps(self, data):
        step = self.step
        for step in step:
            if step == "add":
                self.Calc.add(data)
            elif step == "divTwo":
                with pytest.raises(ZeroDivisionError):
                    self.Calc.div(2, 0)


