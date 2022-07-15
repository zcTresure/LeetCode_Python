# -*- coding: utf-8 -*-
# File:    1217. 玩筹码.py
# Date:    2022/7/15
# Software: Pycharm
from collections import Counter
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        cnt = Counter(p % 2 for p in position)  # 根据模 2 后的余数来统计奇偶个数
        return min(cnt[0], cnt[1])


print(Solution().minCostToMoveChips(position=[1, 2, 3]))
