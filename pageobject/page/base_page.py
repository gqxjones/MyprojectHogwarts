#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    # _base_url = "https://work.weixin.qq.com/wework_admin/frame"
    _base_url = ''

    # 参数中的driver要指定类型
    def __init__(self, driver: WebDriver = None):
        if driver is None:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=chrome_options)
            self._driver.implicitly_wait(5)
            # self._driver = webdriver.Chrome()
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)
