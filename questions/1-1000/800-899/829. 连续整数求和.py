# -*- coding: utf-8 -*-
# File:      829. 连续整数求和.py
# DATA:      2022/6/3
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    # 暴力 + 时间超限
    def consecutiveNumbersSum(self, n: int) -> int:
        ans = 1
        left, right = 1, 2
        tmp = left + right
        while left < right and left < n and right < n:
            print(left, right, tmp)
            if tmp < n:
                right += 1
                tmp += right
            elif tmp > n:
                tmp -= left
                left += 1
            else:
                ans += 1
                tmp -= left
                left += 1
        return ans

    # 数学
    def consecutiveNumbersSum(self, n: int) -> int:
        def isKConsecutive(n: int, k: int) -> int:
            if k % 2 == 0:
                return n % k == 0
            return n % k and 2 * n % k == 0

        ans, k = 0, 1
        while k * (k + 1) <= n * 2:
            if isKConsecutive(n, k):
                ans += 1
            k += 1
        return ans


print(Solution().consecutiveNumbersSum(n=15))
