#!/usr/bin/env python
#-*- coding:utf-8 -*-


from selenium import webdriver
from selenium.webdriver import TouchActions
from time import sleep


class TestTouchAction():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
    
    def test_touchaction_scrollbottom(self):
        '''
        打开chrome
        打开百度网页
        向搜索框中输入‘selenium测试’
        通过 TouchAction 点击搜索框
        滑动到底部，点击下一页
        关闭chrome
        :return:
        '''
        self.driver.get("https://www.baidu.com")
        ele = self.driver.find_element_by_id('kw')
        el_search = self.driver.find_element_by_id('su')

        ele.send_keys('selenium测试')
        action = TouchActions(self.driver)
        action.tap(el_search)
        action.perform()

        action.scroll_from_element(ele, 0 ,10000).perform()
        sleep(3)