# -*- coding: utf-8 -*-
# File:      1886. 判断矩阵经轮转后是否一致.py
# DATA:      2022/6/25
# Software:  PyCharm
from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        for k in range(4):
            for i in range(n):
                for j in range(i, n):
                    mat[j][i], mat[i][j] = mat[i][j], mat[j][i]

            for i in range(n):
                mat[i].reverse()
            if mat == target:
                return True
        return False


print(Solution().findRotation(mat=[[0, 1], [1, 0]], target=[[1, 0], [0, 1]]))
print(Solution().findRotation(mat=[[0, 1], [1, 1]], target=[[1, 0], [0, 1]]))
print(Solution().findRotation(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]], target=[[1, 1, 1], [0, 1, 0], [0, 0, 0]]))
