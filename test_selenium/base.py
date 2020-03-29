#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
import os

class Base():
    def setup(self):
        #处理多浏览器
        # browser = os.getenv("browser")
        # if browser == 'firefox':
        #     self.driver = webdriver.Firefox()
        # else:
        #     self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()