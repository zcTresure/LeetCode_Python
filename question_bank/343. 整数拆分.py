# 对于的正整数 n，当 n >= 2 时，可以拆分成至少两个正整数的和。
# 令 kk 是拆分出的第一个正整数，则剩下的部分是 n - k，n - k以不继续拆分
# 或者继续拆分成至少两个正整数的和。由于每个正整数对应的最大乘积取决于比它小的正整数对应的最大乘积，因此可以使用动态规划求解。

class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 3:
            return n - 1
        dp = [0] * (n + 1)
        dp[1], dp[2], dp[3] = 1, 2, 3
        for i in range(4, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i - j] * dp[j])
        return dp[n]


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), dp[i - j] * j)
        return dp[n]


class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = max(2 * (i - 2), 2 * dp[i - 2], 3 * dp[i - 3])
        return dp[n]


class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        quotient, remainder = n // 3, n % 3
        if remainder == 0:
            return 3 ** quotient
        elif remainder == 1:
            return 3 ** (quotient - 1) * 4
        else:
            return 3 ** quotient * 2


print(Solution.integerBreak(1, 10))
