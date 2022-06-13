# -*- coding: utf-8 -*-
# File:      1572. 矩阵对角线元素的和.py
# DATA:      2022/6/13
# Software:  PyCharm
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0
        mid = n // 2
        for i in range(n):
            total += mat[i][i] + mat[i][n - 1 - i]
        return total - mat[mid][mid] * (n & 1)


print(Solution().diagonalSum(mat=[[1, 2, 3],
                                  [4, 5, 6],
                                  [7, 8, 9]]))
