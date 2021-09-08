# -*- coding: utf-8 -*-
# File:      502. IPO.py
# DATA:      2021/9/8
# Software:  PyCharm
__author__ = 'zcFang'

import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if (w >= max(capital)):
            return w + sum(heapq.nlargest(k, profits))
        curr, n = 0, len(profits)
        arr = list(zip(capital, profits))
        arr.sort(key=lambda x: x[0])
        print(arr)
        pq = []
        for _ in range(k):
            while curr < n and arr[curr][0] <= w:
                heapq.heappush(pq, -arr[curr][1])
                curr += 1
            if (pq):
                w -= heapq.heappop(pq)
            else:
                break
        return w


k, w = 2, 0
capital = [0, 1, 1]
profits = [1, 2, 3]
print(Solution().findMaximizedCapital(k, w, profits, capital))
