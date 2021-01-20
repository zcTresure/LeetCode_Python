# Date:       2021/1/20
# Coding:      UTF-8
__author__ = "zcTresure"

from typing import List, Tuple
import bisect


class DisjointSetUnion:
    def __init__(self, n):
        self.n = n
        self.rank = [1] * n
        self.f = list(range(n))

    def find(self, x: int) -> int:
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]

    def unionSet(self, x: int, y: int) -> bool:
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False

        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx

        self.rank[fx] += self.rank[fy]
        self.f[fy] = fx
        return True


class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [float("inf")] * n
        self.idRec = [-1] * n
        self.lowbit = lambda x: x & (-x)

    def update(self, pos: int, val: int, identity: int):
        while pos > 0:
            if self.tree[pos] > val:
                self.tree[pos] = val
                self.idRec[pos] = identity
            pos -= self.lowbit(pos)

    def query(self, pos: int) -> int:
        minval, j = float("inf"), -1
        while pos < self.n:
            if minval > self.tree[pos]:
                minval = self.tree[pos]
                j = self.idRec[pos]
            pos += self.lowbit(pos)
        return j


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = list()

        def build(pos: List[Tuple[int, int, int]]):
            pos.sort()
            a = [y - x for (x, y, _) in pos]
            b = sorted(set(a))
            num = len(b)

            bit = BIT(num + 1)
            for i in range(n - 1, -1, -1):
                poss = bisect.bisect(b, a[i])
                j = bit.query(poss)
                if j != -1:
                    dis = abs(pos[i][0] - pos[j][0]) + abs(pos[i][1] - pos[j][1])
                    edges.append((dis, pos[i][2], pos[j][2]))
                bit.update(poss, pos[i][0] + pos[i][1], i)

        def solve():
            pos = [(x, y, i) for i, (x, y) in enumerate(points)]
            build(pos)
            pos = [(y, x, i) for i, (x, y) in enumerate(points)]
            build(pos)
            pos = [(-y, x, i) for i, (x, y) in enumerate(points)]
            build(pos)
            pos = [(x, -y, i) for i, (x, y) in enumerate(points)]
            build(pos)

        solve()
        dsu = DisjointSetUnion(n)
        edges.sort()

        ret, num = 0, 1
        for length, x, y in edges:
            if dsu.unionSet(x, y):
                ret += length
                num += 1
                if num == n:
                    break

        return ret


points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
test = Solution()
print(test.minCostConnectPoints(points))
