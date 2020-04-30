#!/usr/bin/env python
#-*- coding:utf-8 -*-

from xueqiuTest.page.base_page import BasePage
from xueqiuTest.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.steps("../page/main.yaml")
        return Market(self._driver)