# -*- coding: utf-8 -*-
# File:      1672. 最富有客户的资产总量.py
# DATA:      2022/4/14
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(account) for account in accounts])


accounts = [[1, 5], [7, 3], [3, 5]]
print(Solution().maximumWealth(accounts))
