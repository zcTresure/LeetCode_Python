# -*- coding: utf-8 -*-
# File:    1688. 比赛中的配对次数.py
# Date:    2022/2/14
# Software: Pycharm
__author__ = 'zcFang'


class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n > 1:
            if n % 2 == 0:
                ans += n // 2
                n //= 2
            else:
                ans += (n - 1) // 2
                n = (n - 1) // 2 + 1
        return ans


print(Solution().numberOfMatches(n=7))
