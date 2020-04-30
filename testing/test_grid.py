#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote

class TestGrid:
    def test_grid(self):
        hub_url = "http://127.0.0.1:4444/wd/hub"
        capability = DesiredCapabilities.CHROME.copy()
        for i in range(1,5):
            driver = Remote(command_executor=hub_url, desired_capabilities=capability)
            driver.get("https://baidu.com")

        driver.execute_script("return JSON.stringify(window.performance.timing)")