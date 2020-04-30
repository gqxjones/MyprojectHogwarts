#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
import yaml

from pageobject.page.base_page import BasePage
from app.page.app import App


class TestApp(BasePage):

    def setup(self):
        self.appmain = App().main()

    @pytest.mark.parametrize("username,gender,phonenum", yaml.safe_load("../data.yml"))
    def test_addcontact(self, username, gender, phonenum):
        var = self.appmain.goto_addressList.click_addmember
