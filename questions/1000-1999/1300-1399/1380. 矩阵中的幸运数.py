# -*- coding: utf-8 -*-
# File:    1380. 矩阵中的幸运数.py
# Date:    2022/2/15
# Software: Pycharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        min_row = [min(row) for row in matrix]
        max_col = [max(col) for col in zip(*matrix)]
        ans = []
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                if x == min_row[i] and x == max_col[j]:
                    ans.append(matrix[i][j])
        return ans


print(Solution().luckyNumbers(matrix=[[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
