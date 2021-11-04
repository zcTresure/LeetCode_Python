# -*- coding: utf-8 -*-
# File:      407. 接雨水 II.py
# DATA:      2021/11/3
# Software:  PyCharm
__author__ = 'zcFang'

import heapq
from collections import deque
from typing import List


class Solution:
    # 最小堆
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        if m <= 2 or n <= 2:
            return 0
        visited = [[0 for _ in range(n)] for _ in range(m)]
        pq = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    visited[i][j] = 1
                    heapq.heappush(pq, (heightMap[i][j], i * n + j))
        ans = 0
        dirs = [-1, 0, 1, 0, -1]
        while pq:
            height, position = heapq.heappop(pq)
            for k in range(4):
                nx, ny = position // n + dirs[k], position % n + dirs[k + 1]
                if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0:
                    if height > heightMap[nx][ny]:
                        ans += height - heightMap[nx][ny]
                    visited[nx][ny] = 1
                    heapq.heappush(pq, (max(height, heightMap[nx][ny]), nx * n + ny))

        return ans

    # 广度优先搜索
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        if m <= 2 or n <= 2:
            return 0
        max_height = max(max(row) for row in heightMap)
        water = [[max_height for _ in range(n)] for _ in range(m)]
        dirs = [-1, 0, 1, 0, -1]
        pq = deque()
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    if water[i][j] > heightMap[i][j]:
                        water[i][j] = heightMap[i][j]
                        pq.append([i, j])

        while pq:
            x, y = pq.popleft()
            for i in range(4):
                nx, ny = x + dirs[i], y + dirs[i + 1]
                if 0 <= nx < m and 0 <= ny < n and water[x][y] < water[nx][ny] and water[nx][ny] > heightMap[nx][ny]:
                    water[nx][ny] = max(water[x][y], heightMap[nx][ny])
                    pq.append([nx, ny])
        ans = sum((water[i][j] - heightMap[i][j]) for i in range(m) for j in range(n))
        return ans


heightMap = [[1, 4, 3, 1, 3, 2],
             [3, 2, 1, 3, 2, 4],
             [2, 3, 3, 2, 3, 1]]
print(Solution().trapRainWater(heightMap))
