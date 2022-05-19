# -*- coding: utf-8 -*-
# File:      668. 乘法表中第k小的数.py
# DATA:      2022/5/18
# Software:  PyCharm
__author__ = 'zcFang'

from bisect import bisect_left


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        return bisect_left(range(m * n), k, key=lambda x: x // n * n + sum(x // i for i in range(x // n + 1, m + 1)))

    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left, right = 1, m * n
        while left < right:
            mid = (left + right) >> 1
            if self.cnt(mid, m, n) < k:
                left = mid + 1
            else:
                right = mid
        return left

    def cnt(self, mid: int, m: int, n: int) -> int:
        res, i, j = 0, m, 1
        while i >= 1 and j <= n:
            if i * j <= mid:
                res += i
                j += 1
            else:
                i -= 1
        return res



print(Solution().findKthNumber(m=3, n=3, k=5))
