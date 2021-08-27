# -*- coding: utf-8 -*-
# File:      295. 数据流的中位数.py
# DATA:      2021/8/27
# Software:  PyCharm
__author__ = 'zcFang'

import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.que_min = list()
        self.que_max = list()

    def addNum(self, num: int) -> None:
        que_min = self.que_min
        que_max = self.que_max
        if not que_min or num <= -que_min[0]:  # 小于最小堆
            heapq.heappush(que_min, -num)  # 入队
            if len(que_max) + 1 < len(que_min):  #
                heapq.heappush(que_max, -heapq.heappop(que_min))
        else:
            heapq.heappush(que_max, num)
            if len(que_max) > len(que_min):
                heapq.heappush(que_min, -heapq.heappop(que_max))

    def findMedian(self) -> float:
        que_min = self.que_min
        que_max = self.que_max
        if len(que_min) > len(que_max):
            return -que_min[0]
        return (-que_min[0] + que_max[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
