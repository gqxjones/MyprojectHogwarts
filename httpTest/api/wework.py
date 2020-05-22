#!/usr/bin/env python
# -*- coding:utf-8 -*-
from httpTest.api.base_api import BaseApi


class weWork(BaseApi):
    id = 'ww5c26515c581b70fd'

    def get_token(self, secrete):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": self.id,
                "corpsecret": secrete
            }
        }
        return self.send_api(data)['access_token']