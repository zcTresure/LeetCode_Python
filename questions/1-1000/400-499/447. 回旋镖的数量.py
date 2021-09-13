# -*- coding: utf-8 -*-
# File:      447. 回旋镖的数量.py
# DATA:      2021/9/13
# Software:  PyCharm
__author__ = 'zcFang'

from collections import defaultdict
from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for p1 in points:
            cnt = defaultdict(int)
            for p2 in points:
                dis = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
                cnt[dis] += 1
            for m in cnt.values():
                ans += m * (m - 1)
        return ans


points = [[1, 0], [2, 0], [0, 0]]
print(Solution().numberOfBoomerangs(points))
