# -*- coding: utf-8 -*-
# File:      521. 最长特殊序列 Ⅰ.py
# DATA:      2022/3/5
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return max(len(a), len(b)) if a != b else -1


print(Solution().findLUSlength(a='aba', b='cdc'))
