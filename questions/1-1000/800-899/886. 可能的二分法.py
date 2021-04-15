# File Name:  886. 可能的二分法
# date:       2021/3/26
# encode:      UTF-8
__author__ = 'zcTresure'

from collections import defaultdict
from typing import List


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in dislikes:  # 建立无向图
            graph[u].append(v)
            graph[v].append(u)
        color = {}  # 给图上的点上颜色

        def dfs(node, c=0):
            if node in color:  # 点出现过，判断是否为和之前一样的颜色
                return color[node] == c
            color[node] = c  # 该点没有出现过，标记
            return all(dfs(nei, c ^ 1) for nei in graph[node])

        return all(dfs(node) for node in range(1, N + 1) if node not in color)


N = 5
dislike = [[1, 2], [2, 3], [3, 4], [4, 5]]
test = Solution()
print(test.possibleBipartition(N, dislike))
