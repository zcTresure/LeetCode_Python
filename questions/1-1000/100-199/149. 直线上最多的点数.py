# -*- coding: utf-8 -*-
# File:     149. 直线上最多的点数.py
# Date:     2021/6/25
# Software: PyCharm
__author__ = 'zcFang'

from collections import Counter
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # 三点在一条直线上时,斜率相等
        # y2 - y1 = k * (x2 - x1), y3 - y2 = k * (x3 - x2)
        # (y2 - y1) * (x3 - x2) = (y3 - y2) * (x2 - x1)

        explored = set()
        ans = 1
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                curr = 2
                dx, dy = points[j][0] - points[i][0], points[j][1] - points[i][1]
                for k in range(j + 1, len(points)):
                    if (i, j) in explored or (i, k) in explored or (j, k) in explored:
                        continue
                    if dy * (points[k][0] - points[j][0]) == (points[k][1] - points[j][1]) * dx:
                        curr += 1
                        explored.add((j, k))
                        explored.add((i, k))
                ans = max(ans, curr)
        return ans

    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(m, n):
            return m if not n else gcd(n, m % n)

        def getslope(p1, p2):
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]

            if dx == 0: return (p1[0], 0)
            if dy == 0: return (0, p1[1])

            d = gcd(dx, dy)
            return (dx // d, dy // d)

        res = 0
        for i in range(len(points)):
            d = defaultdict(lambda: 0)
            same, maxi = 1, 0
            p1 = points[i]
            for j in range(i + 1, len(points)):
                p2 = points[j]
                if p1 == p2:
                    same += 1
                else:
                    slope = getslope(p1, p2)
                    d[slope] += 1
                    maxi = max(maxi, d[slope])
            res = max(res, same + maxi)

        return res



points = [[1, 1], [2, 2], [3, 3]]
print(Solution().maxPoints(points))
