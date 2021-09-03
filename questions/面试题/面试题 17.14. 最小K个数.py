# -*- coding: utf-8 -*-
# File:      面试题 17.14. 最小K个数.py
# DATA:      2021/9/3
# Software:  PyCharm
__author__ = 'zcFang'

import heapq
from typing import List


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans


arr = [1, 3, 5, 7, 2, 4, 6, 8]
k = 4
print(Solution().smallestK(arr, k))
