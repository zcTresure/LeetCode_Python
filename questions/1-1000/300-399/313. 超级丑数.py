# -*- coding: utf-8 -*-
# File:      313. 超级丑数.py
# DATA:      2021/8/9
# Software:  PyCharm
__author__ = 'zcFang'

import heapq
from typing import List


class Solution:
    @classmethod
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        seen = {1}
        heap = [1]
        ugly_num = 0
        for i in range(n):
            ugly_num = heapq.heappop(heap)
            for prime in primes:
                next = ugly_num * prime
                if next not in seen:
                    seen.add(next)
                    heapq.heappush(heap, next)
        return ugly_num


n = 12
primes = [2, 7, 13, 19]
print(Solution.nthSuperUglyNumber(n, primes))
