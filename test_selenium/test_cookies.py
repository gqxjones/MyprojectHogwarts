#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
1.使用复用浏览器技术获取企业微信的cookie，点击添加成员
'''

import json
from typing import List, Dict
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDebugSele:
    def setup(self):
        # 浏览器复用
        chrome_options = webdriver.ChromeOptions()
        chrome_options.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=chrome_options)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    # 浏览器复用
    @pytest.mark.skip
    def test_getcookies(self):
        cookies = self.driver.get_cookies()
        with open("cookies.txt", "w") as f:
            json.dump(cookies, f)

    # cookies使用
    def test_cookies(self):
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        with open("cookies.txt", "r") as f:
            cookies: List[Dict] = json.load(f)
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_item').click()
