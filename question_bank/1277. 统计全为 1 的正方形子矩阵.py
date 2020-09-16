class Solution:
    def countSquares(self, matrix: list) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        dp = list(matrix)
        for i in range(1, m):
            for j in range(1, n):
                if dp[i][j] != 0 and matrix[i - 1][j - 1] != 0 and dp[i][j - 1] != 0 and dp[i - 1][j] != 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        for i in range(m):
            for j in range(n):
                ans += dp[i][j]
        return ans

    def countSquares(self, matrix: list) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                elif matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                ans += dp[i][j]
        return ans


matrix = [[0, 1, 1, 1],
          [1, 1, 1, 1],
          [0, 1, 1, 1]]
print(Solution().countSquares(matrix))
