# -*- coding: utf-8 -*-
# File:      1606. 找到处理最多请求的服务器.py
# DATA:      2022/3/30
# Software:  PyCharm
__author__ = 'zcFang'

import heapq
from typing import List

from sortedcontainers import SortedList


class Solution:
    # 模拟 + 有序集合 + 优先队列
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = SortedList(range(k))
        busy = []
        requests = [0] * k
        for i, (start, t) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                available.add(busy[0][1])
                heapq.heappop(busy)
            if len(available) == 0:
                continue
            j = available.bisect_left(i % k)
            if j == len(available):
                j = 0
            id = available[j]
            requests[id] += 1
            heapq.heappush(busy, (start + t, id))
            available.remove(id)
            print(available, busy)
        maxRequest = max(requests)
        return [i for i, request in enumerate(requests) if request == maxRequest]

    # 模拟 + 双优先队列
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = list(range(k))
        busy = []
        requests = [0] * k
        for i, (start, t) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                _, id = heapq.heappop(busy)
                heapq.heappush(available, i + (id - i) % k)
            if available:
                id = heapq.heappop(available) % k
                requests[id] += 1
                heapq.heappush(busy, (start + t, id))
        maxRequest = max(requests)
        return [i for i, request in enumerate(requests) if request == maxRequest]


k = 3
arrival = [1, 2, 3, 4, 5]
load = [5, 2, 3, 3, 3]
print(Solution().busiestServers(k, arrival, load))
print(4 + (3 - 4) % 6)
