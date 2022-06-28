# Date:       2021/3/16
# encode:      UTF-8
__author__ = "zcTresure"

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or len(matrix) == 1:
            return matrix[0]
        ans = []
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, cols = len(matrix), len(matrix[0])
        row, col, dirIdx = 0, 0, 0
        visited = [[False] * cols for _ in range(rows)]
        for i in range(rows * cols):
            ans.append(matrix[row][col])
            visited[row][col] = True
            r, c = row + dirs[dirIdx][0], col + dirs[dirIdx][1]
            if not (0 <= r < rows and 0 <= c < cols and not visited[r][c]):
                dirIdx = (dirIdx + 1) % 4
            row, col = row + dirs[dirIdx][0], col + dirs[dirIdx][1]
        return ans


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test = Solution()
print(test.spiralOrder(matrix))
