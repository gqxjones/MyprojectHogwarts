#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pageobject.page.main import Main


class TestRegister:
    def setup(self):
        self.main = Main()

    def test_addMember(self):
        add_member = self.main.goto_add_member()
        add_member.add_member()
        add_member.get_first()
        assert add_member.get_first() == 'ricebug'
