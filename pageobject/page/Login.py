#!/usr/bin/env python
#-*- coding:utf-8 -*-

from pageobject.page.base_page import BasePage
from selenium.webdriver.common.by import By
from pageobject.page.Register import Register

class Login(BasePage):
    def scan(self):
        pass
    def goto_register(self):
        self.find(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return Register(self._driver)