# -*- coding: utf-8 -*-
# File:    1787. 使所有区间的异或结果为零.py
# Date:    2021/5/25
# Software: Pycharm
__author__ = 'zcFang'

from collections import Counter
from typing import List


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        MAXX = 2 ** 10  # x 的范围为 [0, 2^10)
        n = len(nums)
        f = [float("inf")] * MAXX
        f[0] = 0  # 边界条件 f(-1,0)=0
        for i in range(k):
            # 第 i 个组的哈希映射
            count = Counter()
            size = 0
            for j in range(i, n, k):
                count[nums[j]] += 1
                size += 1
            t2min = min(f)  # 求出 t2
            g = [t2min] * MAXX
            for mask in range(MAXX):
                for x, countx in count.items():  # t1 则需要枚举 x 才能求出
                    g[mask] = min(g[mask], f[mask ^ x] - countx)
            f = [val + size for val in g]  # 别忘了加上 size
        return f[0]


nums = [3, 4, 5, 2, 1, 7, 3, 4, 7]
k = 3
test = Solution()
print(test.minChanges(nums, k))
