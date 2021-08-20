# -*- coding: utf-8 -*-
# File:      541. 反转字符串 II.py
# DATA:      2021/8/20
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        t = list(s)
        for i in range(0, len(t), 2 * k):
            t[i:i + k] = reversed(t[i:i + k])
        return ''.join(t)


print(Solution().reverseStr('abcdefg', 2))
