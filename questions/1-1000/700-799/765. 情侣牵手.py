# -*- coding: utf-8 -*-
# File:      765. 情侣牵手.py
# DATA:      2021/9/9
# Software:  PyCharm
__author__ = 'zcFang'

from collections import defaultdict
from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        res = 0
        for i in range(0, n - 1, 2):
            if row[i] == row[i + 1] ^ 1:
                continue
            for j in range(i + 1, n):
                if row[i] == row[j] ^ 1:
                    row[i + 1], row[j] = row[j], row[i + 1]
            res += 1
        return res

    def minSwapsCouples(self, row: List[int]) -> int:
        dic = defaultdict()
        ans = 0
        for i in range(len(row)):
            dic[row[i]] = i
        for i in range(0, len(row), 2):
            lover = row[i] ^ 1
            if (dic[lover]) != i + 1:
                ans += 1
                dic[row[i + 1]] = dic[lover]
                row[dic[lover]], row[i + 1] = row[i + 1], row[dic[lover]]
                dic[lover] = i + 1
        return ans


row = [3, 2, 1, 0]
print(Solution().minSwapsCouples(row))
