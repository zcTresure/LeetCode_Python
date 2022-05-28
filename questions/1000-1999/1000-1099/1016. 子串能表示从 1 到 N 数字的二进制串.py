# -*- coding: utf-8 -*-
# File:      1016. 子串能表示从 1 到 N 数字的二进制串.py
# DATA:      2022/5/28
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def queryString(self, s: str, n: int) -> bool:
        res = True
        if n < 2:
            return res
        for i in range(n >> 1 + 1, n + 1):
            bins = bin(i)[2:]
            if bins not in s:
                return False
        return True


# s = "10010111100001110010"
# n = 10
s = "0110"
n = 4
print(Solution().queryString(s, n))
