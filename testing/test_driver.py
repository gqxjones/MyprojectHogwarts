#!/usr/bin/env python
#-*- coding:utf-8 -*-

from selenium import webdriver
import pytest
import time

def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    driver.find_element_by_id("kw").send_keys("allure")
    time.sleep(2)
    driver.find_element_by_id("su").click()
    time.sleep(3)
    driver.quit()