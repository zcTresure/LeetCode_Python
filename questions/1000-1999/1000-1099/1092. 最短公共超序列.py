# -*- coding: utf-8 -*-
# File:      1092. 最短公共超序列.py
# DATA:      2021/9/15
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        # 最长公共子串
        dp = [[""] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                else:
                    if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 1]
        lcs = dp[m][n]
        ans = ""
        i, j = 0, 0
        # 添加头部和公共子串
        for c in lcs:
            while i < m and str1[i] != c:
                ans += str1[i]
                i += 1
            while j < n and str2[j] != c:
                ans += str2[j]
                j += 1
            ans += c
            i += 1
            j += 1
        # 补充尾部字串
        return ans + str1[i:] + str2[j:]


str1 = "abac"
str2 = "cab"
print(Solution().shortestCommonSupersequence(str1, str2))
