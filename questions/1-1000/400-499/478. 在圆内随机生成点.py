# -*- coding: utf-8 -*-
# File:      478. 在圆内随机生成点.py
# DATA:      2022/6/5
# Software:  PyCharm
__author__ = 'zcFang'

import random
from typing import List


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x = x_center
        self.y = y_center
        self.r = radius

    def randPoint(self) -> List[float]:
        while True:
            x, y = random.uniform(-self.x, self.r), random.uniform(-self.r, self.r)
            if x * x + y * y <= self.x * self.y:
                return [self.x + x, self.y + y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
