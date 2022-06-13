# -*- coding: utf-8 -*-
# File:      1051. 高度检查器.py
# DATA:      2022/6/13
# Software:  PyCharm
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(x != y for x, y in zip(heights, sorted(heights)))


print(Solution().heightChecker(heights=[1, 1, 4, 2, 1, 3]))
