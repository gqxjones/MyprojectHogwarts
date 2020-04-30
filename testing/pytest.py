#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
pytest的参数化
'''

import pytest
from python.Calc import Calc

def setup_module():
    print("setup_module")


class TestCalc:
    # 调用之后被执行一次
    @classmethod
    def setup_class(cls):
        print("setup_class")

    # setup_method setup teardown teardown_method每次执行test都会被执行
    def setup_method(self):
        print("setup_method")

    def setup(self):
        print("setup")
        self.Calc = Calc()

    def teardown(self):
        print("teardown")

    def teardown_method(self):
        print("teardown method")

    @pytest.mark.parametrize('result, a, b', [
        (2, 0, 2),
        (3, 1, 2),
        (0, -1, 1)
    ])

    #order需要与zadd一起使用才能生效
    # @pytest.mark.run(order=-1)
    def test_zaddOne(self, result, a, b):
        # assert self.Calc.add(0, 2) == 2
        assert self.Calc.add(a, b) == result

if __name__ == '__main__':
    # pytest.main("-v TestCalc")
    pytest.main(['-v', 'TestCalc'])