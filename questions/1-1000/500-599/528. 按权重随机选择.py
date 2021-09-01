# -*- coding: utf-8 -*-
# File:      528. 按权重随机选择.py
# DATA:      2021/8/30
# Software:  PyCharm
__author__ = 'zcFang'

from bisect import bisect_left
import random
from typing import List
from itertools import accumulate


class Solution:

    def __init__(self, w: List[int]):
        self.pre = list(accumulate(w))
        self.total = sum(w)

    def pickIndex(self) -> int:
        x = random.randint(1, self.total)
        return bisect_left(self.pre, x)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
