# -*- coding: utf-8 -*-
# File:      709. 转换成小写字母.py
# DATA:      2021/12/12
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def toLowerCase(self, s: str) -> str:
        return "".join(chr(asc | 32) if 65 <= (asc := ord(ch)) <= 90 else ch for ch in s)

    def toLowerCase(self, s: str) -> str:
        return s.lower()


s = 'ACMDF'
print(Solution().toLowerCase(s))
