#!/usr/bin/env python
# -*- coding:utf-8 -*-


import logging
from typing import List
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage():
    _black_list = [
        (MobileBy.XPATH, "//*[@text='确定']"),
        (MobileBy.XPATH, "//*[@text='允许']")
    ]

    _error_num = 0
    _error_max = 3

    def __init__(self, driver:WebDriver = None):
        self._driver = driver

    # def find(self, locator, value):
    #     try:
    #         if isinstance(locator, tuple):
    #             return self._driver.find_element(*locator)
    #         else:
    #             return self._driver.find_elements(locator, value)
    #     except Exception as e:
    #         if self._error_num > self._error_max:
    #             raise e
    #         self._error_num += 1
    #         for ele in self._black_list:
    #             elelist = self._driver.find_elements(*ele)
    #             if len(elelist) > 0:
    #                 elelist[0].click()
    #                 self.find(locator, value)
    #         raise e

    def find(self, by, locator=None):
        try:
            if isinstance(by, tuple):
                return self._driver.find_element(*by)
            else:
                return self._driver.find_elements(by, locator)
        except Exception as e:
            self._error_num += 1
            if self._error_num > self._error_max:
                raise e
            for ele in self._black_list:
                elelist = self._driver.find_elements(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    self.find(by, locator)
            raise e

    def send(self,value, by, locator=None):
        try:
            self.find(by, locator).send_keys()
        except Exception as e:
            self._error_num += 1
            if self._error_num > self._error_max:
                raise e
            for ele in self._black_list:
                elelist = self._driver.find_elements(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    return self.send(value, by, locator)
            raise e


    def steps(self, file):
        with open(file, encoding='utf-8') as f:
            steps: List[dict] = yaml.safe_load(f)
            for step in steps:
                if 'by' in step.keys():
                    if step['by'] == 'id':
                        element = self.find(step['by'], step['locator'])
                    if step['by'] == 'xpath':
                        element = self.find(MobileBy.XPATH, step['locator'])
                if 'action' in step.keys():
                    action = step['action']
                    if action == 'find':
                        pass
                    elif action == 'click':
                        element.click()
                    elif action == 'send':
                        content:str = step["value"]
                        for param in self.params:
                            content = content.replace({"%s"}%param, self.params[param])
                        element.send_keys(content)