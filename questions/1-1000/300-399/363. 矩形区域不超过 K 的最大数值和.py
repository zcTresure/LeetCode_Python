# File Name:  363. 矩形区域不超过 K 的最大数值和
# date:       2021/4/22
# encode:      UTF-8
__author__ = 'zcTresure'

from bisect import bisect_left, insort
from typing import List


class Solution:
    # 朴素二维前缀和
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ans = float("-inf")
        m, n = len(matrix), len(matrix[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = prefix[i + 1][j] + prefix[i][j + 1] - prefix[i][j] + matrix[i][j]

        print(prefix)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for p in range(m + 1):
                    for q in range(n + 1):
                        # 矩阵和  =   右下角    -    左下角        -      右上角        +     左上角
                        cur = prefix[p][q] - prefix[i - 1][q] - prefix[p][j - 1] + prefix[i - 1][j - 1]
                        if cur <= k:
                            ans = max(ans, cur)
        return ans

    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ans = float("-inf")
        m, n = len(matrix), len(matrix[0])

        for i in range(m):  # 枚举上边界
            total = [0] * n
            for j in range(i, m):  # 枚举下边界
                for c in range(n):
                    total[c] += matrix[j][c]  # 更新每列的元素和
                presum = [0]
                s = 0
                for v in total:
                    s += v
                    index = bisect_left(presum, s - k)
                    if index != len(presum):
                        ans = max(ans, s - presum[index])
                    insort(presum, s)

        return ans


matrix = [[2, 2, -1]]
k = -1
test = Solution()
print(test.maxSumSubmatrix(matrix, k))
