#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
pytest的基本使用
'''

from python.Calc import Calc

class TestCalc:
    def test_addOne(self):
        calc = Calc()
        assert calc.add(0, 2) == 2

    def test_addTwo(self):
        calc = Calc()
        assert calc.add(1, 2) == 3

    def test_addThree(self):
        calc = Calc()
        assert calc.add(-2, 1) == -1

    def test_addFour(self):
        calc = Calc()
        assert calc.add(2, -1) == 1

    def test_addFive(self):
        calc = Calc()
        assert calc.add(2, 0) == 2

    def test_addSix(self):
        calc = Calc()
        assert calc.add(0.01, 2) == 2.01

    def test_addSeven(self):
        calc = Calc()
        assert calc.add(1, 2) != 2

    #除法
    def test_divOne(self):
        calc = Calc()
        assert calc.div(0, 2) == 0

    def test_divTwo(self):
        calc = Calc()
        assert calc.div(1, 10) == 0.1

    def test_divThree(self):
        calc = Calc()
        assert calc.div(-2, 1) == -2

    def test_divFour(self):
        calc = Calc()
        assert calc.div(2, -1) == -2

    def test_divFive(self):
        calc = Calc()
        assert calc.div(5.5, 5) == 1.1

    def test_divSix(self):
        calc = Calc()
        try:
            calc.div(2, 0)
        except Exception as e:
            print(e)

    def test_divSeven(self):
        calc = Calc()
        assert calc.div(2, 2) != 2