# -*- coding: utf-8 -*-
# File:      2100. 适合打劫银行的日子.py
# DATA:      2022/3/6
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    # 动态规划
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        up, down = [0] * n, [0] * n
        for i in range(1, n):
            # 第 i 天不小于 i - 1 天的警卫的数量
            if security[i - 1] >= security[i]:
                up[i] = up[i - 1] + 1
            # 第 n - i - 1 天不大于 n - i  天警卫的数量
            if security[n - i - 1] <= security[n - i]:
                down[n - i - 1] = down[n - i] + 1
        return [i for i in range(time, n - time) if up[i] >= time and down[i] >= time]


security = [5, 3, 3, 3, 5, 6, 2]
time = 2
print((Solution().goodDaysToRobBank(security, time)))
