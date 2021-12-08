# -*- coding: utf-8 -*-
# File:      1034. 边界着色.py
# DATA:      2021/12/7
# Software:  PyCharm
__author__ = 'zcFang'

from collections import deque
from typing import List, Tuple


class Solution:
    # 深度优先搜索
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        borders = []
        original_color = grid[row][col]
        visited[row][col] = True
        self.dfs(row, col, grid, visited, borders, original_color)
        for x, y in borders:
            grid[x][y] = color
        return grid

    def dfs(self, x: int, y: int, grid: List[List[int]], visited: List[List[bool]], borders: List[List[int]],
            original_color: int):
        is_border = False
        m, n = len(grid), len(grid[0])
        direct = ((-1, 0), (1, 0), (0, -1), (0, 1))
        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < m and 0 <= ny < n and grid[nx][ny] == original_color):
                is_border = True
            elif not visited[nx][ny]:
                visited[nx][ny] = True
                self.dfs(nx, ny, grid, visited, borders, original_color)
        if is_border:
            borders.append([x, y])

    # 广度优先搜索
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        borders = []
        original_color = grid[row][col]
        visited[row][col] = True
        direct = ((-1, 0), (1, 0), (0, -1), (0, 1))
        q = deque([(row, col)])
        while q:
            x, y = q.popleft()
            is_border = False
            for dx, dy in direct:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n and grid[nx][ny] == original_color):
                    is_border = True
                elif not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
            if is_border:
                borders.append((x, y))
        for x, y in borders:
            grid[x][y] = color
        return grid


grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
row, col = 1, 1
color = 3
print(Solution().colorBorder(grid, row, col, color))
