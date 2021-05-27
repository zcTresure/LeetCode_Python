# -*- coding: utf-8 -*-
# File:     461. 汉明距离.py
# Date:     2021/5/27
# Software: PyCharm
__author__ = 'zcFang'


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0
        while x or y:
            cnt += ((x % 2) ^ (y % 2))
            x >>= 1
            y >>= 1
        return cnt

    def hammingDistance(self, x: int, y: int) -> int:
        return len([b for b in bin(x ^ y) if b == '1'])


x, y = 1, 4
test = Solution()
print(test.hammingDistance(x, y))
