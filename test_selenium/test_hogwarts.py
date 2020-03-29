#!/usr/bin/env python
#-*- coding:utf-8 -*-

from selenium import webdriver
from time import sleep

class TestHogwarts():
    
    def setup(self):
        self.driver = driver = webdriver.Chrome()
        self.driver.maximize_window()
         #隐式等待
        self.driver.implicitly_wait(5)
    
    def teardown(self):
        self.driver.quit()

    def test_hogwarts(self):
        self.driver.get("https://home.testing-studio.com/")
        self.driver.find_element_by_link_text("社团").click()
        # self.driver.find_element_by_link_text("社团").click()

        