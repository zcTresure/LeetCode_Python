# File Name:  1719. 重构一棵树的方案数
# date:       2021/4/15
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List


class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        Edge = [[False for _ in range(501)] for _ in range(501)]  # 邻接矩阵
        adj = [set() for _ in range(501)]  # 邻接表
        nodes = set()  # 点集
        for x, y in pairs:  # 初始化时，按照双向图
            Edge[x][y] = True
            Edge[y][x] = True
            adj[x].add(y)
            adj[y].add(x)
            nodes.add(x)
            nodes.add(y)
        nodes = list(nodes)
        nodes.sort(key=lambda x: -len(adj[x]))  # 按出度降序排序
        n = len(nodes)
        if len(adj[nodes[0]]) != n - 1:  # 出度最大的点，出度不是n-1
            return 0  # 没有符合条件的
        res = 1  # 否则，res先置1
        start = 1
        while start < n and len(adj[nodes[start]]) == n - 1:
            res = 2  # 若多个点的出度为n-1  结果为0或2
            start += 1  # 找到最后一个出度为n-1的idx
        for i in range(start):
            x = nodes[i]
            for y in adj[x]:  # y为x指向的点
                adj[y].remove(x)  # 只留x-->y，y指向x的remove掉
        for i in range(start, n):
            x = nodes[i]
            k = len(adj[x])  # x的出度
            for y in adj[x]:  # y为x指向的点
                if len(adj[y]) == k:  # y的出度也为k,x与y可以互换
                    res = 2  # x与y出度相同，res为0或2，先置2
                adj[y].remove(x)  # 删除y指向x的指针（箭头）
                if k < len(set(adj[x]) | set(adj[y])):
                    # x指向的点的个数 < 儿子y和孙子指向的个数
                    return 0
        return res


pairs = [[1, 2], [2, 3], [1, 3]]
test = Solution()
print(test.checkWays(pairs))
