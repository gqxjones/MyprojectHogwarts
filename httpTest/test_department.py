#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests


class TestDepartment:
    secrete = 'rjLxujzktWgM6gTAWOVYP24m18QBOF3NqNr-tEm78Uw'
    id = 'ww5c26515c581b70fd'

    def setup(self):
        r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.id}&corpsecret={self.secrete}')
        self.token = r.json()['access_token']

    def test_department(self):
        createDate = {
            "name": "CD研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1,
            "id": 2
        }
        # 创建部门
        create_department = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token='+self.token, json=createDate)
        if create_department.json()['errcode'] == 0:
            # 获取部门
            get_department = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token='+self.token+'&id=1')
            print(get_department.json())
            assert get_department.json()['errcode'] == 0

        # 更新部门
        updateDate = {
            "id": 2,
            "name": "CD研发中心RICE",
            "name_en": "RDGZ1"
        }
        update_department = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token='+self.token, json=updateDate)
        print(update_department.json())

        # 删除部门
        delete_department = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token='+self.token+'&id=2')
        print(delete_department.json())
        assert delete_department.json()['errcode'] == 0
