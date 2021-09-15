# -*- coding: utf-8 -*-
# File:      1079. 活字印刷.py
# DATA:      2021/9/15
# Software:  PyCharm
__author__ = 'zcFang'

import math
from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        dp, cv, all_len = [1] + [0] * len(tiles), Counter(tiles).values(), 0
        for v in cv:
            all_len += v
            for i in range(all_len, 0, -1):
                dp[i] += sum(dp[i - j] * math.comb(i, j) for j in range(1, min(i, v) + 1))
        return sum(dp) - 1


tiles = "AAB"
print(Solution().numTilePossibilities(tiles))
