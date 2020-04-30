#!/usr/bin/env python
# -*- coding:utf-8 -*-
from app.page.memberInvitePage import MemberInvitePage
from pageobject.page.base_page import BasePage

class AddressListPage(BasePage):

    def click_addmember(self):
        return MemberInvitePage(self._driver)