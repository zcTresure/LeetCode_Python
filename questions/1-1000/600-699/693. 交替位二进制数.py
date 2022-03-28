# -*- coding: utf-8 -*-
# File:      693. 交替位二进制数.py
# DATA:      2022/3/28
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    # 模拟
    def hasAlternatingBits(self, n: int) -> bool:
        prev = 2
        while n:
            cur = n % 2
            if cur == prev:
                return False
            prev = cur
            n //= 2
        return True

    # 位运算
    def hasAlternatingBits(self, n: int) -> bool:
        a = n ^ (n >> 1)
        return a & (a + 1) == 0


print(Solution().hasAlternatingBits(n=10))
