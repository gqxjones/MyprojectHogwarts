#!/usr/bin/env python
# -*- coding:utf-8 -*-
from app.page.contactAddpage import ContactAddpage
from pageobject.page.base_page import BasePage

class MemberInvitePage(BasePage):

    def click_menualadd(self):
        return  ContactAddpage(self._driver)