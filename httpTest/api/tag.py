#!/usr/bin/env python
# -*- coding:utf-8 -*-

from httpTest.api.base_api import BaseApi
from httpTest.api.wework import weWork


class Tag(BaseApi):
    secrete = 'T5Hn3BPoiwQ4XZAd3lJTjjoVwKY0I1MlOzs5hVMzKbU'

    def __init__(self):
        self.token = weWork().get_token(self.secrete)

    def add(self, tagname):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            "params": {
                "access_token": self.token
            },
            "json": {
                "group_name": "newRicebug",
                "tag": [{
                    "name": tagname
                }]
            }
        }
        return self.send_api(data)

    def get(self):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            "params": {
                "access_token": self.token
            }
        }
        return self.send_api(data)

    def delete(self, tagid):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params": {
                "access_token": self.token
            },
            "json": {
                "tag_id": [tagid]
            }
        }
        return self.send_api(data)

    def update(self, tagid, name):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
            "params": {
                "access_token": self.token
            },
            "json": {
                "id": tagid,
                "name": name
            }
        }
        return self.send_api(data)
