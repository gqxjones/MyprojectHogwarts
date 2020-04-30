#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _base_url = ''
    _driver = ''
    # 参数中的driver要指定类型
    def __init__(self, reuse = True):
        if reuse == True:
        # if self._driver is None:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=chrome_options)
        else:
            self._driver = webdriver.Chrome()
        if self._base_url != '':
            self._driver.get(self._base_url)
        self._driver.implicitly_wait(5)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def find_elements(self, by, locator):
        return self._driver.find_elements(by, locator)

    def wait_for(self, fun):
        WebDriverWait(self._driver, 10).until(fun)
