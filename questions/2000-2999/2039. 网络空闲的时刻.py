# -*- coding: utf-8 -*-
# File:      2039. 网络空闲的时刻.py
# DATA:      2022/3/20
# Software:  PyCharm
__author__ = 'zcFang'

from collections import deque
from typing import List


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        visited = [False] * n
        visited[0] = True
        q = deque([0])
        ans, dist = 0, 1
        while q:
            for _ in range(len(q)):
                u = q.popleft()
                for v in g[u]:
                    if visited[v]:
                        continue
                    visited[v] = True
                    q.append(v)
                    ans = max(ans, (dist * 2 - 1) // patience[v] * patience[v] + dist * 2 + 1)
            dist += 1
        return ans


edges = [[0, 1], [1, 2]]
patience = [0, 2, 1]
print(Solution().networkBecomesIdle(edges, patience))
