#!/usr/bin/env python
# -*- coding:utf-8 -*-

from appium import webdriver
from time import sleep

class TestBrowser():
    def setup(self):
        desire_cap = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "browserName":"Browser",
            "noReset": "true",
            "chromedriverExecutable":"D:\ITtool\develop\chromedriver.exe",
            "udid": "127.0.0.1:7555" #唯一标识
            #"chromedriverExecutableDir":"D:\ITtool\develop\"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(30)


    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("https://m.baidu.com")
        # self.driver.switch_to.context()
