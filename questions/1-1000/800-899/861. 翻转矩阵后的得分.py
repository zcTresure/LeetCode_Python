# Date:       2020/12/7
# encode:      UTF-8
__author__ = "zcTresure"


class Solution:
    def matrixScore(self, A: list) -> int:
        m, n = len(A), len(A[0])
        # 将所有的第一位算作1 计算
        maxScore, tmp = m * 2 ** (n - 1), 0
        for i in range(1, n):
            for j in range(m):
                if A[j][0] == 0:  # 当前行的第一位为0时，A[j][i] ^ 1，然后统计
                    tmp += 1 ^ A[j][i]
                else:  # 当前行第一位为1时直接统计列中1的个数
                    tmp += A[j][i]
            # count(1) < count(0) 进行0 1翻转
            tmp = max(tmp, m - tmp)
            # 计算该列的最大得分
            maxScore += tmp * 2 ** (n - i - 1)
            tmp = 0
        return maxScore


nums = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
test = Solution()
print(test.matrixScore(nums))
