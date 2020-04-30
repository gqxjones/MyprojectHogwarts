#!/usr/bin/env python
# -*- coding:utf-8 -*-

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desire_cap = {
    "platformName": "Android",
    "deviceName": "127.0.0.1:7555",
    "appPackage": "com.tencent.wework",
    "appActivity": ".launch.LaunchSplashActivity",
    "noReset": "true"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
driver.implicitly_wait(5)
driver.find_element_by_id()
driver.find_element_by_accessibility_id()
el1 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]")
el1.click()
el2 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.TextView")
el2.click()
el3 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView")
el3.click()
el4 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView")
el4.click()
driver.back()
el5 = driver.find_element_by_id("com.tencent.wework:id/gq_")
el5.click()
driver.quit()

def test_touchaction(self):
    action = TouchAction(self.driver)
    window_rect = self.driver.get_window_rect()
    width = window_rect['width']
    height = window_rect['height']
    x1 = int(width/2)
    y_start = int(height * 4/5)
    y_end = int(height * 1/5)
    action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()

