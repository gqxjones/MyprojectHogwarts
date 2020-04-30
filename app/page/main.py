#!/usr/bin/env python
# -*- coding:utf-8 -*-
from app.page.addressListPage import AddressListPage
from app.page.base_page import BasePage


class Main(BasePage):
    def goto_message(self):
        pass

    def goto_addressList(self):
        self.steps('../steps/mainsteps.yml')
        return AddressListPage(self._driver)

    def goto_workbench(self):
        pass

    def goto_profile(self):
        pass