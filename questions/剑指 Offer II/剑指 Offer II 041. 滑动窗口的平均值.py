# -*- coding: utf-8 -*-
# File:    剑指 Offer II 041. 滑动窗口的平均值.py
# Date:    2022/7/16
# Software: Pycharm
from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.sum = 0
        self.q = deque()

    def next(self, val: int) -> float:
        if len(self.q) == self.size:
            self.sum -= self.q.popleft()
        self.sum += val
        self.q.append(val)
        return self.sum / len(self.q)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
