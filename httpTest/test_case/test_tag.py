#!/usr/bin/env python
# -*- coding:utf-8 -*-


import json
from jsonpath import jsonpath
from httpTest.api.tag import Tag
from httpTest.api.wework import weWork


class TestTag:
    def setup(self):
        self.tag = Tag()

    def test_wework(self):
        secrete = 'T5Hn3BPoiwQ4XZAd3lJTjjoVwKY0I1MlOzs5hVMzKbU'
        print(weWork().get_token(secrete))

    def test_get(self):
        print(json.dumps(self.tag.get(), indent=2))

    def test_add(self):
        print(self.tag.add('ricebug3'))

    def test_update(self):
        print(self.tag.update('etQ2y-BgAAjPK2yg_KuFV9y9Tlp5ZdpA', 'ricebugO'))

    def test_delete(self):
        print(self.tag.delete('etQ2y-BgAA60Ma29qZ7U8F9vYBMOwCvg'))

    def test_all(self):
        tagId = jsonpath(self.tag.get(), '$..tag[?(@.name=="ricebug3")].id')

        print(tagId)
        if tagId:
            self.tag.delete(tagId[0])
        print(self.tag.add('ricebugThree'))
        tagIdNew = jsonpath(self.tag.get(), '$..tag[?(@.name=="ricebugThree")].id')[0]
        print(tagIdNew)
        print(self.tag.update(tagIdNew, 'hahahaha'))
