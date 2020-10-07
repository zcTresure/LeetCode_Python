class Solution:
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        dp = [[0, 0, 0] for _ in range(n)]
        dp[0][0] = int(leaves[0] == 'y')
        dp[0][1] = dp[0][2] = dp[1][2] = float('inf')
        for i in range(1, n):
            isRed = int(leaves[i] == 'r')
            isYel = int(leaves[i] == 'y')
            dp[i][0] = dp[i - 1][0] + isYel
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + isRed
            if i >= 2:
                dp[i][2] = min(dp[i - 1][1], dp[i - 1][2]) + isYel
        return dp[n - 1][2]


leaves = "rrryyyrryyyrr"
test = Solution()
print(test.minimumOperations(leaves))
