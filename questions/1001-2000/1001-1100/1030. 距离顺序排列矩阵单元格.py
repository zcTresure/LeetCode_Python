# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "zcTresure"

from collections import defaultdict


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> list:
        res = [(i, j) for i in range(R) for j in range(C)]
        return sorted(res, key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))

    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> list:
        maxDist = max(r0, R - 1 - r0) + max(c0, C - 1 - c0)
        bucket = defaultdict(list)
        dist = lambda r1, c1, r2, c2: abs(r1 - r2) + abs(c1 - c2)
        for i in range(R):
            for j in range(C):
                bucket[dist(i, j, r0, c0)].append([i, j])
        res = list()
        for i in range(maxDist + 1):
            res.extend(bucket[i])
        return res

    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> list:
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        maxDist = max(r0, R - 1 - r0) + max(c0, C - 1 - c0)
        row, col = r0, c0
        res = [[row, col]]
        for dist in range(1, maxDist + 1):
            row -= 1
            for i, (dr, dc) in enumerate(dirs):
                while (i % 2 == 0 and row != r0) or (i % 2 != 0 and col != c0):
                    if 0 <= row < R and 0 <= col < C:
                        res.append([row, col])
                    row += dr
                    col += dc
        return res


R, C = 1, 2
r0 = c0 = 0
test = Solution()
print(test.allCellsDistOrder(R, C, r0, c0))
