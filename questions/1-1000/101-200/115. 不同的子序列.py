# Date:       2021/3/17
# Coding:      UTF-8
__author__ = "zcTresure"


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # m为字符串s的长度 n为字符串t的长度
        m, n = len(s), len(t)
        # 当子串长度大于字符串长度直接返回 0
        if m < n:
            return 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 默认字符串和子串最后一位字符相同
        for i in range(m + 1):
            dp[i][n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # 当 s[i]=t[j]s[i]=t[j] 时，dp[i][j]dp[i][j] 由两部分组成：
                # 如果 s[i] 和 t[j] 匹配，则考虑 t[j+1:] 作为 s[i+1:] 的子序列，子序列数为 dp[i+1][j+1]
                # 如果 s[i] 不和 t[j] 匹配，则考虑 t[j:] 作为 s[i+1:] 的子序列，子序列数为 dp[i+1][j]
                # 因此当 s[i]=t[j] 时，有 dp[i][j]=dp[i+1][j+1]+dp[i+1][j]
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    # 当 s[i] 不等于 t[j] 时，s[i] 不能和 t[j] 匹配，因此只考虑 t[j:] 作为 s[i+1:] 的子序列，子序列数为 dp[i+1][j]
                    # 因此当 s[i] 不等于 t[j] 时，有 dp[i][j]=dp[i+1][j]
                    dp[i][j] = dp[i + 1][j]
        return dp[0][0]


test = Solution()
s = "babgbag"
t = "bag"
print(test.numDistinct(s, t))
