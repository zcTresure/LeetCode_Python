# -*- coding: utf-8 -*-
# File:      441. 排列硬币.py
# DATA:      2021/10/10
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans = 0
        while ans <= n:
            n -= ans
            ans += 1
        return ans - 1

    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (right  + left + 1) // 2
            if mid * (mid + 1) <= 2 * n:
                left = mid
            else:
                right = mid - 1
        return left


n = 8
print(Solution().arrangeCoins(n))
