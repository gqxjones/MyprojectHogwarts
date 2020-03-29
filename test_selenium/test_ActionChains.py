#!/usr/bin/env python
#-*- coding:utf-8 -*-


from selenium import webdriver
from selenium.webdriver import ActionChains
import pytest
from time import sleep

from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_click(self):
        element_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        element_doubleclick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        element_rightclick = self.driver.find_element_by_xpath("//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        action.perform()

    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com")
        ele = self.driver.find_element_by_link_text("设置")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/gragDropMooTools.htm")
        drag_element = self.driver.find_element_by_id("dragger")
        drop_element = self.driver.find_element_by_xpath("/html/body/div[2]")
        action = ActionChains(self.driver)
        # action.drag_and_drop(drag_element, drag_element).perform()
        # action.click_and_hold(drag_element).release(drop_element).perform()
        action.click_and_hold(drag_element).move_to_element(drop_element).release().perform()

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/gragDropMooTools.htm")
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        action = ActionChains(self.driver)
        action.send_keys("username")
        action.send_keys(Keys.SPACE)
        action.send_keys("tom")
        action.send_keys(Keys.BACK_SPACE)
        action.perform()

# if __name__ == '__main__':
#     pytest('-v', '-s')
