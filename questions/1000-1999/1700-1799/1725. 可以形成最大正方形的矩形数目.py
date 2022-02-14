# -*- coding: utf-8 -*-
# File:    1725. 可以形成最大正方形的矩形数目.py
# Date:    2022/2/14
# Software: Pycharm
__author__ = 'zcFang'

from collections import Counter
from typing import List


class Solution:
    # 一次遍历
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        res, maxLen = 0, 0
        for l, w in rectangles:
            k = min(l, w)
            if k == maxLen:
                res += 1
            elif k > maxLen:
                res = 1
                maxLen = k
        return res

    # 一次遍历 + 哈希统计
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        count = Counter(min(rectangle) for rectangle in rectangles)
        return count[max(count.keys())]


print(Solution().countGoodRectangles(rectangles=[[5, 8], [3, 9], [5, 12], [16, 5]]))
print(Solution().countGoodRectangles(rectangles=[[2, 3], [3, 7], [4, 3], [3, 7]]))
