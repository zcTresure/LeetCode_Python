# File Name:  91. 解码方法
# date:       2021/4/21
# encode:      UTF-8
__author__ = 'zcTresure'


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1] + [0] * n
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if i > 1 and s[i - 2] != '0' and int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[n]

    def numDecodings(self, s: str) -> int:
        n = len(s)
        a, b, c = 0, 1, 0
        for i in range(1, n + 1):
            c = 0
            if s[i - 1] != '0':
                c += b
            if i > 1 and s[i - 2] != '0' and int(s[i - 2:i]) <= 26:
                c += a
            a, b = b, c
        return c


s = "2611055971756562"
test = Solution()
print(test.numDecodings(s))
