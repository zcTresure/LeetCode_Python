# -*- coding: utf-8 -*-
# File:      390. 消除游戏.py
# DATA:      2022/1/2
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def lastRemaining(self, n: int) -> int:
        a1, an = 1, n
        k, cnt, step = 0, n, 1
        while cnt > 1:
            if k % 2 == 0:
                a1 += step
                if cnt % 2:
                    an -= step
            else:
                if cnt % 2:
                    a1 += step
                an -= step
            k += 1
            cnt >>= 1
            step <<= 1
        return a1


n = int(input())
print(Solution().lastRemaining(n))
