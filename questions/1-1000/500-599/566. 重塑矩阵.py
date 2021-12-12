# -*- coding: utf-8 -*-
# File:      566. 重塑矩阵.py
# DATA:      2021/12/11
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        ans = [[0] * c for _ in range(r)]
        for x in range(m * n):
            ans[x // c][x % c] = mat[x // n][x % n]
        return ans


mat = [[1, 2], [3, 4]]
r = 1
c = 4
print(Solution().matrixReshape(mat, r, c))
