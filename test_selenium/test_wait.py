#!/usr/bin/env python
#-*- coding:utf-8 -*-

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwarts():

    def setup(self):
        self.driver = driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://home.testing-studio.com/')
        # 隐式等待
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()
    
    def test_wait(self):
        self.driver.find_element(By.XPATH, '//*[@title="归入各种类别的所有主题"]').click()
        # sleep(3)强制等待
        #定义等待条件
        def wait(x):
            return len(self.driver.find_elements(By.XPATH, '//*[@class="table-heading"]')) >= 1
        # 传递函数不能使用wait()
        # WebDriverWait(self.driver, 10).until(wait)
        #使用Python自带的方法
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@class="table-heading"]')))
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()
        