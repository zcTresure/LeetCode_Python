# -*- coding: utf-8 -*-
# File:      2028. 找出缺失的观测数据.py
# DATA:      2022/3/27
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        missingSum = mean * (len(rolls) + n) - sum(rolls)
        if not n <= missingSum <= n * 6:
            return []
        quotient, remainder = divmod(missingSum, n)
        return [quotient + 1] * remainder + [quotient] * (n - remainder)


print(Solution().missingRolls(rolls=[1, 5, 6], mean=3, n=4))
