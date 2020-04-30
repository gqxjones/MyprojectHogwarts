#!/usr/bin/env python
#-*- coding:utf-8 -*-

from xueqiuTest.page.base_page import BasePage
from xueqiuTest.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps("../page/market.yaml")
        return Search(self._driver)