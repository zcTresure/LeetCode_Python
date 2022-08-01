# -*- coding: utf-8 -*-
# File:    剑指 Offer II 115. 重建序列.py
# Date:    2022/7/23
# Software: Pycharm
from collections import deque
from itertools import pairwise
from typing import List


class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)
        g = [[] for _ in range(n)]
        inDeg = [0] * n
        for sequence in sequences:
            for x, y in pairwise(sequence):
                g[x - 1].append(y - 1)
                inDeg[y - 1] += 1

        q = deque([i for i, d in enumerate(inDeg) if d == 0])
        while q:
            if len(q) > 1:
                return False
            x = q.popleft()
            for y in g[x]:
                inDeg[y] -= 1
                if inDeg[y] == 0:
                    q.append(y)
        return True


print(Solution().sequenceReconstruction(nums=[1, 2, 3], sequences=[[1, 2], [1, 3]]))
print(Solution().sequenceReconstruction(nums=[1, 2, 3], sequences=[[1, 2]]))
print(Solution().sequenceReconstruction(nums=[1, 2, 3], sequences=[[1, 2], [1, 3], [2, 3]]))
