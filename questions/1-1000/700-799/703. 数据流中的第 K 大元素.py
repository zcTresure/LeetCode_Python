# -*- coding: utf-8 -*-
# File:      703. 数据流中的第 K 大元素.py
# DATA:      2021/12/3
# Software:  PyCharm
__author__ = 'zcFang'

import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.que = nums
        heapq.heapify(self.que)

    def add(self, val: int) -> int:
        heapq.heappush(self.que, val)
        while len(self.que) > self.k:
            heapq.heappop(self.que)
        return self.que[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
