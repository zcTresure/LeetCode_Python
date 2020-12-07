# Date:       2020/12/7
# Coding:      UTF-8
__author__ = "zcTresure"


class Solution:
    def matrixScore(self, A: list) -> int:
        m, n = len(A), len(A[0])
        maxScore, tmp = m * 2 ** (n - 1), 0
        for i in range(1, n):
            for j in range(m):
                if A[j][0] == 0:
                    tmp += 1 ^ A[j][i]
                else:
                    tmp += A[j][i]
            tmp = max(tmp, m - tmp)
            maxScore += tmp * 2 ** (n - i - 1)
            tmp = 0
        return maxScore


nums = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
test = Solution()
print(test.matrixScore(nums))
