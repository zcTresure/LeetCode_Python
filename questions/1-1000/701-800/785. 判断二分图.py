# File Name:  785. 判断二分图
# date:       2021/3/26
# encode:      UTF-8
__author__ = 'zcTresure'

from collections import defaultdict
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        g = defaultdict(list)
        m = len(graph)
        for i in range(m):  # 建立无向图
            for j in range(len(graph[i])):
                g[i].append(graph[i][j])
                g[graph[i][j]].append(i)
        color = {}  # 给图上的点上颜色

        def dfs(node, c=0):
            if node in color:  # 点出现过，判断是否为和之前一样的颜色
                return color[node] == c
            color[node] = c  # 该点没有出现过，标记
            return all(dfs(nei, c ^ 1) for nei in g[node])

        return all(dfs(node) for node in range(m) if node not in color)


graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
graph = [[1,3],[0,2],[1,3],[0,2]]
test = Solution()
print(test.isBipartite(graph))
