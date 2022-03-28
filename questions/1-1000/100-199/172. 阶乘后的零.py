# -*- coding: utf-8 -*-
# File:      172. 阶乘后的零.py
# DATA:      2022/3/25
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        for i in range(5, n + 1, 5):
            while i % 5 == 0:
                i //= 5
                ans += 1
        return ans

    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n:
            n //= 5
            ans += n
        return ans


print(Solution().trailingZeroes(5))
print(Solution().trailingZeroes(10))
