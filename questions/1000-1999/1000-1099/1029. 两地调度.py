# -*- coding: utf-8 -*-
# File:      1029. 两地调度.py
# DATA:      2021/9/14
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        ans, n = 0, len(costs) // 2
        for i in range(n):
            ans += costs[i][0] + costs[i + n][1]
        return ans


costs = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
print(Solution().twoCitySchedCost(costs))
