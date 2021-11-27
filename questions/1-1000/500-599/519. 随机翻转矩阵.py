# -*- coding: utf-8 -*-
# File:      519. 随机翻转矩阵.py
# DATA:      2021/11/27
# Software:  PyCharm
__author__ = 'zcFang'

import random
from typing import List


class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.map = {}

    def flip(self) -> List[int]:
        x = random.randint(0, self.total - 1)
        self.total -= 1
        index = self.map.get(x, x)
        self.map[x] = self.map.get(self.total, self.total)
        return [index // self.n, index % self.n]

    def reset(self) -> None:
        self.total = self.m * self.n
        self.map.clear()

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
