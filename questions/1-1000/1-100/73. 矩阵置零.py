# File Name:  73. 矩阵置零
# date:       2021/3/21
# Coding:      UTF-8
__author__ = 'zcTresure'

from typing import List


class Solution:
    # 使用标记数组
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        row, col = [False] * m, [False] * n  # 标记数组，存储每一个零元素的行和列

        for i in range(m):  # 记录零元素的位置
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = True

        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:  # 将含有零元素的每行每列全都置为零
                    matrix[i][j] = 0

    # 使用栈存储零元素
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        stack = []  # 栈存储每个零元素的位置
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    stack.append((i, j))
        while stack:
            row, column = stack.pop()  # 零元素的位置出栈
            for j in range(n):  # 行置零
                matrix[row][j] = 0
            for i in range(m):  # 列置零
                matrix[i][column] = 0

    # 使用两个标记变量
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        flag_row0 = any(matrix[0][i] == 0 for i in range(n))  # 记录第一列零的位置
        flag_col0 = any(matrix[j][0] == 0 for j in range(m))  # 记录第一行零的位置
        for i in range(1, m):  # 将第二列开始零元素的行和列的第一个元素置为零
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1, m):  # 第一列或第一行有零元素的行列置为零
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if flag_col0:  # 如果原来第一列存在零元素，第一列全置为零
            for i in range(m):
                matrix[i][0] = 0
        if flag_row0:  # 如果原来第一行存在零元素，第一行全置为零
            for j in range(n):
                matrix[0][j] = 0

    # 使用一个标记变量
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        flag_col0 = False  # 记录第一列是否存在零元素
        for i in range(m):
            if matrix[i][0] == 0:  # 记录第一列中是否存在零元素
                flag_col0 = True
            for j in range(1, n):  # 将第二列开始的零元素的行和列第一个元素置为零
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(m - 1, -1, -1):
            for j in range(1, n):  # 第一列或第一行有零元素的行列置为零
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if flag_col0:  # 如果原来第一列存在零元素，第一列全置为零
                matrix[i][0] = 0


matrix = [[0, 1, 2, 0],
          [3, 4, 5, 2],
          [1, 3, 1, 5]]
test = Solution()
test.setZeroes(matrix)
