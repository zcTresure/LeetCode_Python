# File Name:  1143. 最长公共子序列
# date:       2021/4/3
# encode:      UTF-8
__author__ = 'zcTresure'


class Solution:
    # 动态规划
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:  # 字符相同，公共子序列加 1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:  # 字符不同，状态转移
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]


test1 = 'abc'
test2 = 'aunskcsl'
test = Solution()
print(test.longestCommonSubsequence(test1, test2))
