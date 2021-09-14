# -*- coding: utf-8 -*-
# File:      1040. 移动石子直到连续 II.py
# DATA:      2021/9/14
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        min_move = n = len(stones)
        i = 0
        for j in range(n):
            while stones[j] - stones[i] + 1 > n:
                i += 1
            all_stone = j - i + 1
            if all_stone == n - 1 and stones[j] - stones[i] + 1 == n - 1:
                min_move = min(min_move, 2)
            else:
                min_move = min(min_move, n - all_stone)
        return [min_move, max(stones[n - 1] - stones[1], stones[n - 2] - stones[0]) - n + 2]


stones = [6, 5, 4, 3, 10]
print(Solution().numMovesStonesII(stones))
