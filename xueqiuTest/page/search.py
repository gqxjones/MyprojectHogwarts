#!/usr/bin/env python
#-*- coding:utf-8 -*-

from xueqiuTest.page.base_page import BasePage

class Search(BasePage):
    def search(self, value):
        self._params["value"] = value
        self.steps('../page/search.yaml')