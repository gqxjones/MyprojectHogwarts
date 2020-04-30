#!/usr/bin/env python
# -*- coding:utf-8 -*-

from appium import webdriver
from app.page.base_page import BasePage
from app.page.main import Main


class App(BasePage):
    def start(self):
        _appPackage = 'com.tencent.wework'
        _appActivity = '.launch.LaunchSplashActivity'
        if self._driver is None:
            desired_caps = {
                "platformName": "Android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.LaunchSplashActivity",
                "noReset": "true",
                "skipDeviceInitialization": "true",
                "unicodeKeyboard": 'true',
                "resetKeyboard": 'true'
            }
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            self._driver.implicitly_wait(300)
        else:
            self._driver.start_activity(_appPackage, _appActivity)

        return self

    def stop(self):
        self._driver.quit()

    def restart(self):
        pass

    def main(self):
        return Main(self._driver)
