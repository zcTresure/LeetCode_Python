# -*- coding: utf-8 -*-
# File:    871. 最低加油次数.py
# Date:    2022/7/4
# Software: Pycharm
from heapq import heappop, heappush
from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        ans, fuel, prev, h = 0, startFuel, 0, []
        for i in range(n + 1):
            curr = stations[i][0] if i < n else target
            fuel -= curr - prev
            while fuel < 0 and h:
                fuel -= heappop(h)
                ans += 1
            if fuel < 0:
                return -1
            if i < n:
                heappush(h, -stations[i][1])
                prev = curr
        return ans


print(Solution().minRefuelStops(target=1, startFuel=1, stations=[]))
print(Solution().minRefuelStops(target=100, startFuel=1, stations=[[10, 100]]))
print(Solution().minRefuelStops(target=100, startFuel=10, stations=[[10, 60], [20, 30], [30, 30], [60, 40]]))
