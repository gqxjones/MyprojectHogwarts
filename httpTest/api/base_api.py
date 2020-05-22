#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep

import requests


class BaseApi:

    def send_api(self, data:dict):
        return requests.request(**data).json()
