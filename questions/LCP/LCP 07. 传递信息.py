# -*- coding: utf-8 -*-
# File:     LCP 07. 传递信息.py
# Date:     2021/7/1
# Software: PyCharm
__author__ = 'zcFang'

from typing import List
from collections import defaultdict, deque


class Solution:

    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        # 广度优先搜索
        # self.n, self.k, self.ways = n, k, 0
        # self.graph = defaultdict(list)
        # for node1, node2 in relation:
        #     self.graph[node1].append(node2)
        # self.dfs(0, 0)
        # return self.ways

        # 深度优先搜索
        # graph = defaultdict(list)
        # for node1, node2 in relation:
        #     graph[node1].append(node2)
        # steps = 0
        # queue = deque([0])
        # while queue and steps < k:
        #     steps += 1
        #     size = len(queue)
        #     for i in range(len(queue)):
        #         index = queue.popleft()
        #         to = graph[index]
        #         for next_index in to:
        #             queue.append(next_index)
        # ways = 0
        # if steps == k:
        #     while queue:
        #         if queue.popleft() == n - 1:
        #             ways += 1
        # return ways

        # 二维动态规划
        # dp = [[0] * (n + 1) for _ in range(k + 1)]
        # dp[0][0] = 1
        # for i in range(k):
        #     for node1, node2 in relation:
        #         dp[i + 1][node2] += dp[i][node1]
        # return dp[k][n - 1]

        # 一维动态规划
        dp = [1] + [0] * (n - 1)
        for i in range(k):
            next = [0] * n
            for node1, node2 in relation:
                next[node2] += dp[node1]
            dp = next
        return dp[n - 1]

    def dfs(self, index: int, steps: int) -> None:
        if steps == self.k:
            if index == self.n - 1:
                self.ways += 1
            return
        for to in self.graph[index]:
            self.dfs(to, steps + 1)


n = 5
relation = [[0, 2], [2, 1], [3, 4], [2, 3], [1, 4], [2, 0], [0, 4]]
k = 3
print(Solution().numWays(n, relation, k))
