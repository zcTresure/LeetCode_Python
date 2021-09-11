# -*- coding: utf-8 -*-
# File:      600. 不含连续1的非负整数.py
# DATA:      2021/9/11
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def findIntegers(self, n: int) -> int:
        dp = [0] * 31
        dp[0] = dp[1] = 1
        for i in range(2, 31):
            dp[i] = dp[i - 1] + dp[i - 2]
        print(dp)
        ans, pre = 0, 0
        for i in range(29, -1, -1):
            val = (1 << i)
            if n & val:
                n -= val
                ans += dp[i + 1]
                if pre == 1:
                    break
                pre = 1
            else:
                pre = 0

        return ans + 1


print(Solution().findIntegers(5))