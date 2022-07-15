# -*- coding: utf-8 -*-
# File:    1252. 奇数值单元格的数目.py
# Date:    2022/7/15
# Software: Pycharm
from typing import List


class Solution:
    # 直接模拟
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0] * n for _ in range(m)]
        for x, y in indices:
            for j in range(n):
                matrix[x][j] += 1
            for row in matrix:
                row[y] += 1
        return sum(x % 2 for row in matrix for x in row)

    # 模拟空间优化
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n
        for x, y in indices:
            rows[x] += 1
            cols[y] += 1
        return sum((row + col) % 2 for row in rows for col in cols)

    # 计数优化
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n
        for x, y in indices:
            rows[x] += 1
            cols[y] += 1
        oddx = sum(row % 2 for row in rows)
        oddy = sum(col % 2 for col in cols)
        return oddx * (n - oddy) + (m - oddx) * oddy


print(Solution().oddCells(m=2, n=3, indices=[[0, 1], [1, 1]]))
