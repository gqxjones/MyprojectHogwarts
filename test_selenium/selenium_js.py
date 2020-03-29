#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
selenium执行js
'''

import time

from selenium.webdriver import ActionChains

from test_selenium.base import Base
import pytest


class TestJS(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id('kw').send_keys('selenium测试')
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="page"]/a[10]').click()
        time.sleep(3)
        for code in [
            'return document.title', 'return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))
        #另外一种写法
        # self.driver.execute_script('return document.title; return JSON.stringify(performance.timing)')

    @pytest.mark.skip
    def test_datatime(self):
        self.driver.get('https://www.12306.cn/index/')
        self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        time.sleep(3)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))

    @pytest.mark.skip
    def test_file(self):
        self.driver.get('http://image.baidu.com')
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        #图片路径
        self.driver.find_element_by_id('stfile').send_keys("")
        time.sleep(2)

    #alter弹框处理
    def test_alter(self):
        '''
        1
        :return:
        '''
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to_frame('iframeResult')

        drag = self.driver.find_element_by_id('draggable')
        drop = self.driver.find_element_by_id('droppable')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()

        #点击alter
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id('submitBTN').click()
        time.sleep(3)
