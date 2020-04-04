#!/usr/bin/env python
#-*- coding:utf-8 -*-

from pageobject.page.base_page import BasePage
from selenium.webdriver.common.by import By

class Register(BasePage):
    def register(self):
        self.find(By.ID, "corp_name").send_keys("hello")
        self.find(By.ID, "manager_name").send_keys("hello2")
        return True
