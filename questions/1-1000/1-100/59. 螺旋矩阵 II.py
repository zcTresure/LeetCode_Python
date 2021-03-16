# Date:       2021/3/16
# Coding:      UTF-8
__author__ = "zcTresure"

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row, col, dirIdx = 0, 0, 0
        for i in range(n * n):
            matrix[row][col] = i + 1
            dx, dy = dirs[dirIdx]
            r, c = row + dx, col + dy
            if r < 0 or r >= n or c < 0 or c >= n or matrix[r][c] > 0:
                dirIdx = (dirIdx + 1) % 4
                dx, dy = dirs[dirIdx]
            row, col = row + dx, col + dy
            print(matrix)
        return matrix


n = int(input())
test = Solution()
print(test.generateMatrix(n))
