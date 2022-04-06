# -*- coding: utf-8 -*-
# File:      310. 最小高度树.py
# DATA:      2022/4/6
# Software:  PyCharm
__author__ = 'zcFang'

from collections import deque
from typing import List


class Solution:
    # 广度优先搜索
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        parents = [0] * n

        def bfs(start: int):
            visited = [False] * n
            visited[start] = True

            q = deque([start])
            while q:
                x = q.popleft()
                for y in g[x]:
                    if not visited[y]:
                        visited[y] = True
                        parents[y] = x
                        q.append(y)
            return x

        x = bfs(0)
        y = bfs(x)
        path = []
        parents[x] = -1
        while y != -1:
            path.append(y)
            y = parents[y]
        m = len(path)
        return [path[m // 2]] if m % 2 else [path[m // 2 - 1], path[m // 2]]

    # 深度优先搜索
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        parents = [0] * n
        maxDepth, node = 0, -1

        def dfs(x: int, parent: int, depth: int):
            nonlocal maxDepth, node
            if depth > maxDepth:
                maxDepth, node = depth, x
            parents[x] = parent
            for y in g[x]:
                if y != parent:
                    dfs(y, x, depth + 1)

        dfs(0, -1, 1)
        maxDepth = 0
        dfs(node, -1, 1)

        path = []
        while node != -1:
            path.append(node)
            node = parents[node]
        m = len(path)
        return [path[m // 2]] if m % 2 else [path[m // 2 - 1], path[m // 2]]


    # 拓扑排序
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        g = [[] for _ in range(n)]
        deg = [0] * n
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            deg[x] += 1
            deg[y] += 1
        q = [i for i, d in enumerate(deg) if d == 1]
        remain_node = n
        while remain_node > 2:
            remain_node -= len(q)
            tmp = q
            q = []
            for x in tmp:
                for y in g[x]:
                    deg[y] -= 1
                    if deg[y] == 1:
                        q.append(y)
        return q


print(Solution().findMinHeightTrees(n=4, edges=[[1, 0], [1, 2], [1, 3]]))
print(Solution().findMinHeightTrees(n=6, edges=[[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))
