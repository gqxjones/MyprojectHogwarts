#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
自定义case顺序
参考文档：https://blog.csdn.net/waitan2018/article/details/104334932
'''
import pytest
from _pytest.main import Session

def pytest_collection_modifyitems(session: Session, config, items:list):

    items.reverse()
    session.items = items
