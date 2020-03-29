#!/usr/bin/env python
#-*- coding:utf-8 -*-

from time import sleep
from test_selenium.base import Base
import pytest

class TestWindows(Base):
    def test_windows(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_link_text('登录').click()
        print(self.driver.current_window_handle)
        self.driver.find_element_by_link_text('立即注册').click()
        # self.driver.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/a').click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        self.driver.switch_to_window(self.driver.window_handles[-1])
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__userName"]').send_keys("username")
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__phone"]').send_keys('13800000000')
        sleep(2)
        self.driver.switch_to_window(self.driver.window_handles[0])
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()

        self.driver.find_element_by_id('TANGRAM__PSP_10__userName').send_keys("login_username")
        # self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__userName"]').send_keys("login_username")
        # self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__password"]').send_keys("login_password")
        self.driver.find_element_by_id('TANGRAM__PSP_10__password').send_keys("login_password")
        self.driver.find_element_by_id('TANGRAM__PSP_10__submit').click()

        sleep(3)

    #frame的切换
    @pytest.mark.skip
    def test_frame(self):
        self.driver.get("http://www.baidu.com")
        self.driver.switch_to.frame("iframeResult")
        # self.driver.switch_to_frame("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)
        # self.driver.switch_to.parent_frame()
        self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id("submitBTN").text)