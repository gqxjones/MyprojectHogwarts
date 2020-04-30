#!/usr/bin/env python
# -*- coding:utf-8 -*-

from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestAddContact():
    def setup_class(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": "true",
            "skipDeviceInitialization": "true",
            "unicodeKeyboard": 'true',
            "resetKeyboard": 'true'
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(300)

    # def setup(self):
    #     pass
    #
    # def teardown(self):
    #     self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gpp").click()
    @pytest.fixture()
    def add_fixture(self):
        yield
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gpp").click()

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("username, gender, phonenum", [
        ("ricebug1", "女", "1380000002"),
        ("ricebug2", "男", "1380000003")
    ])
    def test_touchaction_unlock(self, add_fixture, username, gender, phonenum):
        # 手动添加成员
        # username = 'ricebug1'
        # gender = '女'
        # phonenum = '13800000002'
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable('
                                 'new UiSelector().scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()

        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/c56').click()
        sleep(2)

        current_act = self.driver.current_activity
        assert ".contact.controller.ContactAddActivity" in current_act
        # 输入姓名
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/..//*[@resource-id='com.tencent.wework:id/ase']").send_keys(
            username)
        # 选择性别
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@text='性别']/..//*[@resource-id='com.tencent.wework:id/ate']").click()
        if gender == '男':
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("男")').click()
        else:
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("女")').click()
        # 输入电话号码
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/emh").send_keys(phonenum)
        # 点击保存
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gq7").click()

        assert "添加成功" in self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
