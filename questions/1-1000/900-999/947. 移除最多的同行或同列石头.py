# Date:       2021/1/15
# encode:      UTF-8
__author__ = "zcTresure"

from typing import List
import collections


class DisjointSetUnion:
    def __init__(self):
        self.f = dict()
        self.rank = dict()

    def find(self, x: int) -> int:
        if x not in self.f:
            self.f[x] = x
            self.rank[x] = 1
            return x
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]

    def unionSet(self, x: int, y: int):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx
        self.rank[fx] += self.rank[fy]
        self.f[fy] = fx

    def numberOfConnectedComponent(self) -> int:
        return sum(1 for x, fa in self.f.items() if x == fa)


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        dsu = DisjointSetUnion()
        for x, y in stones:
            dsu.unionSet(x, y + 10000)
        return len(stones) - dsu.numberOfConnectedComponent()

    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        edge = collections.defaultdict(list)
        for i, (x1, y1) in enumerate(stones):
            for j, (x2, y2) in enumerate(stones):
                if x1 == x2 or y1 == y2:
                    edge[i].append(j)

        def dfs(x: int):
            vis.add(x)
            for y in edge[x]:
                if y not in vis:
                    dfs(y)

        vis = set()
        num = 0
        for i in range(n):
            if i not in vis:
                num += 1
                dfs(i)

        return n - num

    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        edge = collections.defaultdict(list)
        rec = collections.defaultdict(list)
        for i, (x, y) in enumerate(stones):
            rec[x].append(i)
            rec[y + 10000].append(i)
        for vec in rec.values():
            k = len(vec)
            for i in range(1, k):
                edge[vec[i - 1]].append(vec[i])
                edge[vec[i]].append(vec[i - 1])

        def dfs(x: int):
            vis.add(x)
            for y in edge[x]:
                if y not in vis:
                    dfs(y)

        vis = set()
        num = 0
        for i in range(n):
            if i not in vis:
                num += 1
                dfs(i)
        return n - num


stones = [[0, 1], [1, 0], [1, 1]]
test = Solution()
print(test.removeStones(stones))
