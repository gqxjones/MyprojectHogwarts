#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By


class TestWebview:

    def test_webview(self):
        desire_cap = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": "true",
            "chromedriverExecutable": "/Users/apple/Library/Google/chromedriver"
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)
        # window.performance.timing
        self.driver.find_element(By.XPATH, "//*[@text='交易']").click()
        webview = self.driver.contexts[-1]
        print(webview)
        self.driver.switch_to.context(webview)
        sleep(2)
        all_time = self.driver.execute_script("return window.performance.timing")
        response_time = all_time['responseEnd'] - all_time['responseStart']
        print(response_time)

    def test_navigation(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易']").click()
        webview = self.driver.contexts[-1]
        self.driver.switch_to.context(webview)
        before_type = self.driver.execute_script("return window.performance.navigation.type")
        print(before_type)
        self.driver.execute_script("window.location.href='https://www.baidu.com'")
        self.driver.execute_script("window.location.reload()")
        after_type = self.driver.execute_script("return window.performance.navigation.type")
        print(after_type)

    def test_webview2(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易']").click()
        webview = self.driver.contexts[-1]
        self.driver.switch_to.context(webview)
        type = self.driver.execute_script("return window.location.href")
        print(type)
