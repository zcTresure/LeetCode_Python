# -*- coding: utf-8 -*-
# File:      629. K个逆序对数组.py
# DATA:      2021/11/11
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7

        f = [1] + [0] * k
        for i in range(1, n + 1):
            g = [0] * (k + 1)
            for j in range(k + 1):
                g[j] = (g[j - 1] if j - 1 >= 0 else 0) - (f[j - i] if j - i >= 0 else 0) + f[j]
                g[j] %= mod
            f = g

        return f[k]


n = 3
k = 1
print(Solution().kInversePairs(n, k))
