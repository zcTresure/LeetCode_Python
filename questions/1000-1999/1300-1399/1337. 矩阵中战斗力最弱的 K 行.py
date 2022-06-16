# -*- coding: utf-8 -*-
# File:    1337. 矩阵中战斗力最弱的 K 行.py
# Date:    2021/8/1
# Software: Pycharm
__author__ = 'zcFang'

import heapq
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        army = list()
        for i in range(m):
            left, right, pos = 0, n - 1, -1
            while left <= right:
                mid = (left + right) // 2
                if mat[i][mid] == 0:
                    right = mid - 1
                else:
                    pos = mid
                    left = mid + 1
            army.append((pos + 1, i))

        heapq.heapify(army)
        ans = list()
        for i in range(k):
            ans.append(heapq.heappop(army)[1])
        return ans


mat = [[1, 1, 0, 0, 0],
       [1, 1, 1, 1, 0],
       [1, 0, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1]]
k = 3
print(Solution().kWeakestRows(mat, k))
