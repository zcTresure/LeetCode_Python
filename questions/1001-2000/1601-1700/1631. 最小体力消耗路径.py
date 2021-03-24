# Date:       2021/1/29
# encode:      UTF-8
__author__ = "zcTresure"

from typing import List
from collections import deque
import heapq


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        self.setCount = n  # 当前联通分量数

    def findSet(self, x: int) -> int:
        if self.parent[x] == x:  # 查找根节点
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
        self.setCount -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        x, y = self.findSet(x), self.findSet(y)
        return x == y


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        left, right, ans = 0, 10 ** 6 - 1, 0
        while left <= right:
            mid = (left + right) // 2
            q = deque([(0, 0)])
            seen = {(0, 0)}
            while q:
                x, y = q.popleft()
                for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen and abs(
                            heights[x][y] - heights[nx][ny]) <= mid:
                        q.append((nx, ny))
                        seen.add((nx, ny))
            if (m - 1, n - 1) in seen:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        edges = list()
        for i in range(m):
            for j in range(n):
                iden = i * n + j
                if i > 0:
                    edges.append((iden - n, iden, abs(heights[i][j] - heights[i - 1][j])))
                if j > 0:
                    edges.append((iden - 1, iden, abs(heights[i][j] - heights[i][j - 1])))
        edges.sort(key=lambda e: e[2])
        uf = UnionFind(m * n)
        ans = 0
        for x, y, w in edges:
            uf.unite(x, y)
            if uf.connected(0, m * n - 1):
                ans = w
                break
        return ans

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        q = [(0, 0, 0)]
        dist = [0] + [float("inf")] * (m * n - 1)
        seen = set()

        while q:
            d, x, y = heapq.heappop(q)
            iden = x * n + y
            if iden in seen:
                continue
            if (x, y) == (m - 1, n - 1):
                break

            seen.add(iden)
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= nx < m and 0 <= ny < n and max(d, abs(heights[x][y] - heights[nx][ny])) <= dist[nx * n + ny]:
                    dist[nx * n + ny] = max(d, abs(heights[x][y] - heights[nx][ny]))
                    heapq.heappush(q, (dist[nx * n + ny], nx, ny))

        return dist[m * n - 1]


test = Solution()
heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
# heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
# heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
print(test.minimumEffortPath(heights))
