# -*- coding: utf-8 -*-
# File:      1523. 在区间范围内统计奇数数目.py
# DATA:      2022/6/7
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    # 顺序查找，时间超限
    def countOdds(self, low: int, high: int) -> int:
        return len([i for i in range(low, high + 1) if i % 2 == 1])

    # 前缀和
    def countOdds(self, low: int, high: int) -> int:
        return -(-high // 2 + low // 2)


print(Solution().countOdds(low=3, high=7))
print(Solution().countOdds(low=8, high=10))
