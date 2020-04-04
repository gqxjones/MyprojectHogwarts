#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from pageobject.page.Login import Login
from pageobject.page.Register import Register
from pageobject.page.add_member import AddMember
from pageobject.page.base_page import BasePage


class Main(BasePage):
    # _base_url = "https://work.weixin.qq.com/wework_admin/frame"
    def goto_register(self):
        self.find(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(self._driver)

    def goto_login(self):
        self.find(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return Login(self._driver)

    def goto_add_member(self):
        self.find(By.CSS_SELECTOR, ".index_service_cnt_item_title").click()
        return AddMember(self._driver)

    def import_address(self):
        pass
