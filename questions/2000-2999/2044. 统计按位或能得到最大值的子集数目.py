# -*- coding: utf-8 -*-
# File:      2044. 统计按位或能得到最大值的子集数目.py
# DATA:      2022/3/15
# Software:  PyCharm
__author__ = 'zcFang'

from collections import Counter
from functools import reduce
from operator import or_
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or, max_cnt = -1, 0
        for i in range(1, 1 << len(nums)):
            or_val = reduce(or_, (num for j, num in enumerate(nums) if (i >> j) & 1), 0)
            if or_val > max_or:
                max_or, max_cnt = or_val, 1
            elif or_val == max_or:
                max_cnt += 1
        return max_cnt

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or, max_cnt = -1, 0

        def dfs(pos: int, or_val: int) -> None:
            if pos == len(nums):
                nonlocal max_or, max_cnt
                if or_val > max_or:
                    max_or, max_cnt = or_val, 1
                elif or_val == max_or:
                    max_cnt += 1
                return
            dfs(pos + 1, or_val | nums[pos])
            dfs(pos + 1, or_val)

        dfs(0, 0)
        return max_cnt


nums = [3, 1]
# nums = [2, 2, 2]
print(Solution().countMaxOrSubsets(nums))
