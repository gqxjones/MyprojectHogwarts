#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
1.使用复用浏览器技术获取企业微信的cookie，点击添加成员
'''

import json
from selenium import webdriver


class TestDebugSele:
    def setup(self):
        # 浏览器复用
        chrome_options = webdriver.ChromeOptions()
        chrome_options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    # 浏览器复用，获取cookies
    def test_getcookies(self):
        cookies = self.driver.get_cookies()
        with open("cookies.txt", "w") as f:
            json.dump(cookies, f)
