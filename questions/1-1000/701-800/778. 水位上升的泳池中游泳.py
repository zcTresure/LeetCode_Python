# Date:       2021/1/30
# encode:      UTF-8
__author__ = "zcTresure"

from typing import List
from collections import deque


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        self.Count = n

    def findSet(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findSet(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int) -> bool:
        x, y = self.findSet(x), self.findSet(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += 1
        self.Count -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        x, y = self.findSet(x), self.findSet(y)
        return x == y


class Solution:
    def check(self, grid: list, thread: int):
        if grid[0][0] > thread:
            return False
        n = len(grid)
        visited = [[0] * n for _ in range(n)]
        visited[0][0] = 1
        q = deque([(0, 0)])
        while q:
            x, y = q.popleft()
            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and grid[nx][ny] <= thread:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
        return visited[n - 1][n - 1] == 1

    # 二分查找
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        left, right = 0, n * n - 1
        while left < right:
            mid = (left + right) // 2
            if self.check(grid, mid):
                right = mid
            else:
                left = mid + 1
        return left

    # def swimInWater(self, grid: List[List[int]]) -> int:
    #     m, n = len(grid), len(grid[0])
    #     edges = []
    #     for i in range(m):
    #         for j in range(n):
    #             iden = i * n + j
    #             if i > 0:
    #                 edges.append((iden - n, iden, grid[i][j]))
    #             if j > 0:
    #                 edges.append((iden - 1, iden, grid[i][j]))
    #     edges.sort(key=lambda e: e[2])
    #     uf = UnionFind(m * n)
    #     ans = 0
    #     for x, y, w in edges:
    #         uf.unite(x, y)
    #         if uf.connected(0, m * n - 1):
    #             ans = w
    #             break
    #     return ans


test = Solution()
# pull = [[0, 2], [1, 3]]
pull = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
print(test.swimInWater(pull))
