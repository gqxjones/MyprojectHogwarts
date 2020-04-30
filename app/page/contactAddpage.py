#!/usr/bin/env python
# -*- coding:utf-8 -*-
from app.page.memberInvitePage import MemberInvitePage
from pageobject.page.base_page import BasePage


class ContactAddpage(BasePage):

    def input_name(self):
        return self

    def set_gender(self):
        return self

    def input_phone(self):
        return  self

    def click_save(self):
        return MemberInvitePage(self._driver)