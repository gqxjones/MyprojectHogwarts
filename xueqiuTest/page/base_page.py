#!/usr/bin/env python
#-*- coding:utf-8 -*-

import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    _black_list = [(By.ID, "image_cancel")]
    _error_count = 0
    _error_max = 0
    _params ={}
    def __init__(self, drive:WebDriver=None):
        self._driver = drive

    def find(self, by, locator=None):
        try:
            element = self._driver.find_elements(*by) if isinstance(by, tuple) else self._driver.find_elements(by, locator)
            self._error_count = 0
            return element
        except Exception as e:
            self._error_count += 1
            if self._error_count >= self._error_max:
                raise e
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return  self.find(by, locator)
            raise e

    def send(self, value, by, locator=None):
        try:
            self.find(by, locator).send_keys(value)
            self._error_count = 0
        except Exception as e:
            self._error_count += 1
            if self._error_count >= self._error_max:
                raise e
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.send(value, by, locator)
            raise e

    def steps(self, path):
        with open(path, encoding="utf-8") as f:
            steps :list[dict] = yaml.safe_load(f)
            for step in steps:
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    if "click" == step["action"]:
                        element.click()
                    if "send" == step["action"]:
                        content:str = step["value"]
                        for param in self._params:
                            content = content.replace("{%s}"%param, self._params[""])
                        # element.send_keys("value")
                        self.send(content, step["by"], step["locator"])
