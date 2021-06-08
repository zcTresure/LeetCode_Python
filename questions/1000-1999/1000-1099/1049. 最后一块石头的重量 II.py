# -*- coding: utf-8 -*-
# File:     1049. 最后一块石头的重量 II.py
# Date:     2021/6/6
# Software: PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones) / 2
        candidates = {0}
        for stone in stones:
            addition = set()
            for before in candidates:
                if stone + before <= target:
                    addition.add(stone + before)
                candidates = candidates.union(addition)
        return int(2 * (target - max(candidates)))


stones = [1, 1, 4, 2, 2]
print(Solution().lastStoneWeightII(stones))
