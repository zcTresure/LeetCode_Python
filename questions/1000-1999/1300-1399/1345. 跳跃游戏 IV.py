# -*- coding: utf-8 -*-
# File:    1345. 跳跃游戏 IV.py
# Date:    2022/1/23
# Software: Pycharm
__author__ = 'zcFang'

from collections import defaultdict, deque
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        idxSameValue = defaultdict(list)
        for i, a in enumerate(arr):
            idxSameValue[a].append(i)
        visitedIndex = set()
        q = deque()
        q.append([0, 0])
        visitedIndex.add(0)
        while q:
            idx, step = q.popleft()
            if idx == len(arr) - 1:
                return step
            v = arr[idx]
            step += 1
            for i in idxSameValue[v]:
                if i not in visitedIndex:
                    visitedIndex.add(i)
                    q.append([i, step])
            del idxSameValue[v]
            if idx + 1 < len(arr) and (idx + 1) not in visitedIndex:
                visitedIndex.add(idx + 1)
                q.append([idx + 1, step])
            if idx - 1 >= 0 and (idx - 1) not in visitedIndex:
                visitedIndex.add(idx - 1)
                q.append([idx - 1, step])


arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
print(Solution().minJumps(arr))
