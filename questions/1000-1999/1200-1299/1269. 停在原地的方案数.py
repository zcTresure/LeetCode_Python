# File Name:  1269. 停在原地的方案数
# date:       2021/5/13
# encode:      UTF-8
__author__ = 'zcTresure'


class Solution:
    # 动态规划
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10 ** 9 + 7  # 最大数求余
        maxColumn = min(arrLen - 1, steps)  # 距离原点最远距离
        dp = [[0] * (maxColumn + 1) for _ in range(steps + 1)]
        dp[0][0] = 1  # 初始化原点，站在原地不动
        for i in range(1, steps + 1):
            for j in range(maxColumn + 1):
                dp[i][j] = dp[i - 1][j]  # 站在原地不动
                if j - 1 >= 0:  # j-1不小于原点，就可以向左移动一位
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % mod
                if j + 1 <= maxColumn:  # j+1不大于最远距离，就可以向右移动一位
                    dp[i][j] = (dp[i][j] + dp[i - 1][j + 1]) % mod
        return dp[steps][0]


steps = 3
arrLen = 2
test = Solution()
print(test.numWays(steps, arrLen))
