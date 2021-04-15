# File Name:  74. 搜索二维矩阵
# date:       2021/3/30
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1  # 二维数组转化为一维数组计算
        while low <= high:
            mid = (high - low) // 2 + low
            x = matrix[mid // n][mid % n]# 中间数在 mid//n 行 min%n 列
            if x == target:
                return True
            elif x > target:
                high = mid - 1
            else:
                low = mid + 1
        return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13
test = Solution()
print(test.searchMatrix(matrix, target))
