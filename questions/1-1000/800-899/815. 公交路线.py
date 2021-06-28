# -*- coding: utf-8 -*-
# File:     815. 公交路线.py
# Date:     2021/6/28
# Software: PyCharm
__author__ = 'zcFang'

from typing import List
from collections import defaultdict, deque


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:  # 起点就是终点
            return 0
        n = len(routes)  # 公交车的数量
        bus = defaultdict(set)
        for i in range(n):
            for site in routes[i]:
                bus[site].add(i)  # 记录每个站点要经过的公交车

        q = deque()
        visited = [False] * n
        for i in bus[source]:  # 记录起点在不同线路出现
            q.append(i)
            visited[i] = True

        step = 0
        while q:
            cur_len = len(q)  # 当前步数从起点能到达的所有站点
            for _ in range(cur_len):
                i = q.popleft()  # 不同线路i
                for site in routes[i]:  # 可到达的站点
                    if site == target:
                        return step + 1
                    for j in bus[site]:  # 经过site的所有公交车
                        if visited[j] == False:
                            q.append(j)
                            visited[j] = True
            step += 1
        return -1


routes = [[1, 2, 7], [3, 6, 7]]
source, target = 1, 6
print(Solution().numBusesToDestination(routes, source, target))
