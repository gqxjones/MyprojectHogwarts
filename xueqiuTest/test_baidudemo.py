#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pytest
import allure
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


@allure.testcase('https://www.github.com', name='github')
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data1', ['allure', 'pytest', 'unittest'])
def test_steps_demo(test_data1):

    with allure.step("打开百度网页"):
        # driver = webdriver.Chrome("C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com")
        driver.maximize_window()

    with allure.step("输入搜索词：{test_data1}"):
        # driver.find_element_by_id("kw").send_keys(test_data1)
        driver.find_element(By.ID, '#kw').send_keys(test_data1)
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "su").click()
        time.sleep(3)

    with allure.step("保存图片"):
        driver.save_screenshot("./testcase/b.png")
        allure.attach.file("./testcase/b.png", attachment_type=allure.attachment_type.PNG)
    with allure.step("退出网页"):
        driver.quit()