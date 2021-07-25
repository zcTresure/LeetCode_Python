# -*- coding: utf-8 -*-
# File:    1743. 从相邻元素对还原数组.py
# Date:    2021/7/25
# Software: Pycharm
__author__ = 'zcFang'

from collections import defaultdict
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        m = n = len(adjacentPairs)
        n += 1
        cnts = defaultdict(int)
        hashmap = defaultdict(list)
        for a, b in adjacentPairs:
            cnts[a] += 1
            cnts[b] += 1
            hashmap[a].append(b)
            hashmap[b].append(a)
        start = -1
        for i, v in cnts.items():
            if v == 1:
                start = i
                break
        ans = [0] * n
        ans[0] = start
        ans[1] = hashmap[start][0]
        for i in range(2, n):
            x = ans[i - 1]
            for j in hashmap[x]:
                if j != ans[i - 2]:
                    ans[i] = j
        return ans


adjacentPairs = [[2, 1], [3, 4], [3, 2]]
print(Solution().restoreArray(adjacentPairs))
