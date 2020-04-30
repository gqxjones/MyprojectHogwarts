#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from pageobject.page.base_page import BasePage


class AddMember(BasePage):
    def add_member(self):
        # self.find(By.CSS_SELECTOR, ".ww_compatibleTxt_ipt").send_keys('jones')
        self.find(By.ID, 'username').send_keys('ricebug')
        self.find(By.ID, 'memberAdd_acctid').send_keys('adbc')
        self.find(By.ID, 'memberAdd_phone').send_keys('13800000000')
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()

    def get_first(self):
        elements = self.find_elements(By.CSS_SELECTOR, '#member_list td:nth-child(2)')
        titles = []
        for element in elements:
            titles.append(element.get_attribute('title'))
        return titles

    
