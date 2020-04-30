#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from hamcrest import assert_that, equal_to, close_to, contains_string
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestTouchAction():
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": "com.xueqiu.android.common.MainActivity",
            "noReset": "true",
            "skipDeviceInitialization": "true",
            "unicodeKeyboard": 'true',
            "resetKeyboard": 'true'
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(300)

    def teardown(self):
        # self.driver.quit()
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/action_close').click()

    @pytest.mark.skip
    def test_touchaction_unlock(self):
        # 手势操作
        action = TouchAction(self.driver)
        action.press(x=243, y=395).wait(200).move_to(x=721, y=378).wait(200).move_to(x=1190, y=364).wait(200).move_to(
            x=1202, y=859).wait(200) \
            .move_to(x=195, y=1339).wait(200).release().perform()

    def test_myinfo(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        element = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("账号密码")').click()
        locator = element
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))

    def test_getAttr(self):
        search_ele = self.driver.find_element_by_id('com.xueqiu.android:id/tv_search')
        print(search_ele.get_attribute('content-desc'))
        print(search_ele.get_attribute('resource-id'))
        print(search_ele.get_attribute('enabled'))
        print(search_ele.get_attribute('clickable'))
        print(search_ele.get_attribute('bounds'))

    def test_hamrest(self):
        assert_that(10, equal_to(10))
        assert_that(8, close_to(10, 2))
        assert_that("string", contains_string('string'))

    @pytest.mark.parametrize('searchkey, type, price', [
        ('alibaba', 'BABA', 180),
        ('xiaomi', '01810', 10)
    ])
    def test_search(self, searchkey, type, price):
        '''
        1、打开雪球云用
        2、点击搜索框
        3、输入搜索词‘阿里巴巴’
        4、点击第一个搜索词
        5、判断股票价格
        :return:
        '''
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/tv_search').click()
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/search_input_text').send_keys(searchkey)
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/name').click()
        price_element = self.driver.find_element(MobileBy.XPATH,
                                                 f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        # current_price = float(price_element.text)
        current_price = float(price_element.get_attribute('text'))
        # expect_price = 180
        assert_that(price, close_to(current_price, current_price * 0.1))
