# -*- coding: utf-8 -*-
# File:      391. 完美矩形.py
# DATA:      2021/11/16
# Software:  PyCharm
__author__ = 'zcFang'

from collections import defaultdict
from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area = 0
        minX, minY, maxX, maxY = rectangles[0][0], rectangles[0][1], rectangles[0][2], rectangles[0][3]
        cnt = defaultdict(int)
        for rect in rectangles:
            x, y, a, b = rect[0], rect[1], rect[2], rect[3]

            # 每个矩形的面积之和
            area += (a - x) * (b - y)

            # 二维坐标矩形左下角顶点
            minX, minY = min(minX, x), min(minY, y)

            # 二维坐标矩形左下角顶点
            maxX, maxY = max(maxX, a), max(maxY, b)

            # 每个位子的顶点数
            cnt[(x, y)] += 1
            cnt[(x, b)] += 1
            cnt[(a, y)] += 1
            cnt[(a, b)] += 1

        # 面积不同或者最大矩形四个顶点树不唯一
        if area != (maxX - minX) * (maxY - minY) or cnt[(minX, minY)] != 1 or cnt[minX, maxY] != 1 \
                or cnt[maxX, minY] != 1 or cnt[maxX, maxY] != 1:
            return False

        # 删除最大矩形的四个顶点
        del cnt[(minX, minY)], cnt[(minX, maxY)], cnt[(maxX, minY)], cnt[(maxX, maxY)]

        # 最大矩形内部的顶点只有两个或者四个
        return all(c == 2 or c == 4 for c in cnt.values())


rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]
print(Solution().isRectangleCover(rectangles))
