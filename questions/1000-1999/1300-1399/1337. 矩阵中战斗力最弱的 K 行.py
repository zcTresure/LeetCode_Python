# -*- coding: utf-8 -*-
# File:      1337. 矩阵中战斗力最弱的 K 行.py
# DATA:      2021/8/2
# Software:  PyCharm
__author__ = 'zcFang'

import heapq
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        power = list()
        for i in range(m):
            l, r, pos = 0, n - 1, -1
            while l <= r:
                mid = (l + r) // 2
                if mat[i][mid] == 0:
                    r = mid - 1
                else:
                    pos = mid
                    l = mid + 1
            power.append((pos + 1, i))

        heapq.heapify(power)
        ans = list()
        for i in range(k):
            ans.append(heapq.heappop(power)[1])
        return ans


mat = [[1, 1, 0, 0, 0],
       [1, 1, 1, 1, 0],
       [1, 0, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1]]
k = 3
print(Solution().kWeakestRows(mat, k))
