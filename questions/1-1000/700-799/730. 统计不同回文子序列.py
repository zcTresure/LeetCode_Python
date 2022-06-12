# -*- coding: utf-8 -*-
# File:      730. 统计不同回文子序列.py
# DATA:      2022/6/10
# Software:  PyCharm
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        dp = [[[0] * n for _ in range(n)] for _ in range(4)]
        for i, c in enumerate(s):
            dp[ord(c) - ord('a')][i][i] = 1

        for sz in range(2, n + 1):
            for j in range(sz - 1, n):
                i = j - sz + 1
                for k, c in enumerate("abcd"):
                    if s[i] == c and s[j] == c:
                        dp[k][i][j] = (2 + sum(d[i + 1][j - 1] for d in dp)) % MOD
                    elif s[i] == c:
                        dp[k][i][j] = dp[k][i][j - 1]
                    elif s[j] == c:
                        dp[k][i][j] = dp[k][i + 1][j]
                    else:
                        dp[k][i][j] = dp[k][i + 1][j - 1]
        return sum(d[0][n - 1] for d in dp) % MOD

    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for sz in range(2, n + 1):
            for j in range(sz - 1, n):
                i = j - sz + 1
                if s[i] == s[j]:
                    low, high = i + 1, j - 1
                    while low <= high and s[low] != s[i]:
                        low += 1
                    while high >= low and s[high] != s[j]:
                        high -= 1
                    if low > high:
                        dp[i][j] = (2 + dp[i + 1][j - 1] * 2) % MOD
                    elif low == high:
                        dp[i][j] = (1 + dp[i + 1][j - 1] * 2) % MOD
                    else:
                        dp[i][j] = (dp[i + 1][j - 1] * 2 - dp[low + 1][high - 1]) % MOD
                else:
                    dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % MOD
        return dp[0][n - 1]


print(Solution().countPalindromicSubsequences(s='abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'))
