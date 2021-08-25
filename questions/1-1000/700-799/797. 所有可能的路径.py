# -*- coding: utf-8 -*-
# File:      797. 所有可能的路径.py
# DATA:      2021/8/25
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        stk = []

        def dfs(x: int):
            if x == len(graph) - 1:
                ans.append(stk[:])
                return
            for y in graph[x]:
                stk.append(y)
                dfs(y)
                stk.pop()

        stk.append(0)
        dfs(0)
        return ans


graph = [[1, 2], [3], [3], []]
print(Solution().allPathsSourceTarget(graph))
