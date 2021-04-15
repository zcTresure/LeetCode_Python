# Date:       2020/12/27
# encode:      UTF-8
__author__ = "zcTresure"

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        left = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    left[i][j] = 1 + (0 if j == 0 else left[i][j - 1])
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                width = left[i][j]
                area = width
                for k in range(i - 1, -1, -1):
                    width = min(width, left[k][j])
                    area = max(area, width * (i - k + 1))
                maxArea = max(maxArea, area)
        return maxArea

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        left = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    left[i][j] = 1 + (0 if j == 0 else left[i][j - 1])
        maxArea = 0
        for j in range(n):
            up, down = [0] * m, [0] * m
            stk = []
            for i in range(m):
                while stk and left[stk[-1]][j] >= left[i][j]:
                    stk.pop()
                up[i] = stk[-1] if stk else -1
                stk.append(i)
            stk = []
            for i in range(m - 1, -1, -1):
                while stk and left[stk[-1]][j] >= left[i][j]:
                    stk.pop()
                down[i] = stk[-1] if stk else m
                stk.append(i)
            for i in range(m):
                height = down[i] - up[i] - 1
                area = height * left[i][j]
                maxArea = max(maxArea, area)
        return maxArea


matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
test = Solution()
print(test.maximalRectangle(matrix))