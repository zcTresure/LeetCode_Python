# -*- coding: utf-8 -*-
# File:      1108. IP 地址无效化.py
# DATA:      2022/6/21
# Software:  PyCharm


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]');