#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep
import requests


class TestWework:
    secrete = 'rjLxujzktWgM6gTAWOVYP24m18QBOF3NqNr-tEm78Uw'
    id = 'ww5c26515c581b70fd'

    def setup(self):
        r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.id}&corpsecret={self.secrete}')
        self.token = r.json()['access_token']

    def test_wework_api(self):

        get_member = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=' + self.token + '&userid=XiaoMi1')
        assert get_member.json()['errcode'] == 0

        data = {
            "userid": 'XiaoMi1',
            "name": 'ricebug'
        }
        update_member = requests.post('https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token='+self.token, json=data)
        print(update_member.json())


