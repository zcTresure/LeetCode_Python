class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0:
            return 1.0
        dp = [0.0] * (K + W)
        # 在 K <= x <= N 分之间的概率都可以作 1 处理
        for i in range(K, min(N, K + W - 1) + 1):
            dp[i] = 1.0
        for i in range(K - 1, -1, -1):
            for j in range(1, W + 1):
                dp[i] += dp[i + j] / W
            print(dp)
        return dp[0]

    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0:
            return 1.0
        dp = [0.0] * (K + W)
        for i in range(K, min(N, K + W - 1) + 1):
            dp[i] = 1.0
        dp[K - 1] = float(min(N - K + 1, W)) / W
        for i in range(K - 2, -1, -1):
            dp[i] = dp[i + 1] - (dp[i + W + 1] - dp[i + 1]) / W
        return dp[0]


N, K, W = 10, 1, 10
N, K, W = 6, 1, 10
N, K, W = 21, 17, 10
test = Solution()
print(test.new21Game(N, K, W))
