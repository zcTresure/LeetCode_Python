# -*- coding: utf-8 -*-
# File:      851. 喧闹和富有.py
# DATA:      2021/12/15
# Software:  PyCharm
__author__ = 'zcFang'

from collections import deque
from typing import List


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        gr = [[] for _ in range(n)]
        for r in richer:
            gr[r[1]].append(r[0])

        ans = [-1] * n

        def dfs(x: int):
            if ans[x] != -1:
                return
            ans[x] = x
            for y in gr[x]:
                dfs(y)
                if quiet[ans[y]] < quiet[ans[x]]:
                    ans[x] = ans[y]

        for i in range(n):
            dfs(i)
        return ans

    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        g = [[] for _ in range(n)]
        inDeg = [0] * n
        for r in richer:
            g[r[0]].append(r[1])
            inDeg[r[1]] += 1

        ans = list(range(n))
        q = deque(i for i, deg in enumerate(inDeg) if deg == 0)
        while q:
            x = q.popleft()
            for y in g[x]:
                if quiet[ans[x]] < quiet[ans[y]]:
                    ans[y] = ans[x]  # 更新 x 的邻居的答案
                inDeg[y] -= 1
                if inDeg[y] == 0:
                    q.append(y)
        return ans


richer = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]]
quiet = [3, 2, 5, 4, 6, 1, 7, 0]
print(Solution().loudAndRich(richer, quiet))
