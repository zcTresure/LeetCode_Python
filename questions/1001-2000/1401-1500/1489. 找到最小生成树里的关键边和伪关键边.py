# Date:       2021/1/21
# Coding:      UTF-8
__author__ = "zcTresure"

from typing import List
import collections


# 并查集模板
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        # 当前连通分量数目
        self.setCount = n

    def findset(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        return x == y


# Tarjan 算法求桥边模版
class TarjanSCC:
    def __init__(self, n: int, edges: List[List[int]], edgesId: List[List[int]]):
        self.n = n
        self.edges = edges
        self.edgesId = edgesId
        self.low = [-1] * n
        self.dfn = [-1] * n
        self.ans = list()
        self.ts = -1

    def getCuttingEdge(self) -> List[int]:
        for i in range(self.n):
            if self.dfn[i] == -1:
                self.pGetCuttingEdge(i, -1)
        return self.ans

    def pGetCuttingEdge(self, u: int, parentEdgeId: int):
        self.ts += 1
        self.low[u] = self.dfn[u] = self.ts
        for v, iden in zip(self.edges[u], self.edgesId[u]):
            if self.dfn[v] == -1:
                self.pGetCuttingEdge(v, iden)
                self.low[u] = min(self.low[u], self.low[v])
                if self.low[v] > self.dfn[u]:
                    self.ans.append(iden)
            elif iden != parentEdgeId:
                self.low[u] = min(self.low[u], self.dfn[v])


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        m = len(edges)
        for i, edge in enumerate(edges):
            edge.append(i)
        edges.sort(key=lambda x: x[2])

        # 计算 value
        uf_std = UnionFind(n)
        value = 0
        for i in range(m):
            if uf_std.unite(edges[i][0], edges[i][1]):
                value += edges[i][2]

        ans = [list(), list()]

        for i in range(m):
            # 判断是否是关键边
            uf = UnionFind(n)
            v = 0
            for j in range(m):
                if i != j and uf.unite(edges[j][0], edges[j][1]):
                    v += edges[j][2]
            if uf.setCount != 1 or (uf.setCount == 1 and v > value):
                ans[0].append(edges[i][3])
                continue

            # 判断是否是伪关键边
            uf = UnionFind(n)
            uf.unite(edges[i][0], edges[i][1])
            v = edges[i][2]
            for j in range(m):
                if i != j and uf.unite(edges[j][0], edges[j][1]):
                    v += edges[j][2]
            if v == value:
                ans[1].append(edges[i][3])

        return ans

    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        m = len(edges)
        for i, edge in enumerate(edges):
            edge.append(i)
        edges.sort(key=lambda x: x[2])

        uf = UnionFind(n)
        ans0 = list()
        label = [0] * m

        i = 0
        while i < m:
            # 找出所有权值为 w 的边，下标范围为 [i, j)
            w = edges[i][2]
            j = i
            while j < m and edges[j][2] == edges[i][2]:
                j += 1

            # 存储每个连通分量在图 G 中的编号
            compToId = dict()
            # 图 G 的节点数
            gn = 0

            for k in range(i, j):
                x = uf.findset(edges[k][0])
                y = uf.findset(edges[k][1])
                if x != y:
                    if x not in compToId:
                        compToId[x] = gn
                        gn += 1
                    if y not in compToId:
                        compToId[y] = gn
                        gn += 1
                else:
                    # 将自环边标记为 -1
                    label[edges[k][3]] = -1

            # 图 G 的边
            gm = collections.defaultdict(list)
            gmid = collections.defaultdict(list)

            for k in range(i, j):
                x = uf.findset(edges[k][0])
                y = uf.findset(edges[k][1])
                if x != y:
                    idx, idy = compToId[x], compToId[y]
                    gm[idx].append(idy)
                    gmid[idx].append(edges[k][3])
                    gm[idy].append(idx)
                    gmid[idy].append(edges[k][3])

            bridges = TarjanSCC(gn, gm, gmid).getCuttingEdge()
            # 将桥边（关键边）标记为 1
            ans0.extend(bridges)
            for iden in bridges:
                label[iden] = 1

            for k in range(i, j):
                uf.unite(edges[k][0], edges[k][1])

            i = j

        # 未标记的边即为非桥边（伪关键边）
        ans1 = [i for i in range(m) if label[i] == 0]

        return [ans0, ans1]
