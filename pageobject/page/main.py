#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from pageobject.page.Login import Login
from pageobject.page.Register import Register
from pageobject.page.add_member import AddMember
from pageobject.page.base_page import BasePage


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"
    def goto_register(self):
        self.find(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(reuse = True)

    def goto_login(self):
        self.find(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return Login(reuse = True)

    def goto_add_member(self):
        self.find(By.CSS_SELECTOR, ".index_service_cnt_item_title").click()
        def wait():
            ele_len = len(self.find(By.ID, "username"))
            if ele_len < 1:
                self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1) .js_add_member").click()
            # 如果username存在，就返回true
            return ele_len >= 1
        self.wait_for(wait)
        return AddMember(reuse = True)

    def import_address(self):
        pass
