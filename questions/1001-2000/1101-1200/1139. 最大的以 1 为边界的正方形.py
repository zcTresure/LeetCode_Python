class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[[1, 1] if grid[i][j] == 1 else [0, 0]
               for j in range(n)] for i in range(m)]
        largest_len = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                if j != 0:
                    dp[i][j][0] += dp[i][j - 1][0]
                if i != 0:
                    dp[i][j][1] += dp[i - 1][j][1]
                if dp[i][j][0] > largest_len and dp[i][j][1] > largest_len:
                    length_max = min(dp[i][j][0], dp[i][j][1])
                    for length in range(largest_len + 1, length_max + 1):
                        if (dp[i][j + 1 - length][1] >= length) and (dp[i + 1 - length][j][0] >= length):
                            largest_len = length
        return largest_len**2

    def largest1BorderedSquare(self, grid: list) -> int:
        m, n = len(grid), len(grid[0])
        # l表示点i,j左侧连续0的个数，u表示i,j上方连续0的个数
        l = [[0 for _ in range(n)] for _ in range(m)]
        u = [[0 for _ in range(n)] for _ in range(m)]
        maxLen = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                l[i][j], u[i][j] = 1, 1
                if i > 0:
                    u[i][j] += u[i - 1][j]
                if j > 0:
                    l[i][j] += l[i][j - 1]
                for k in range(min(u[i][j], l[i][j]), 0, -1):
                    if k > maxLen and u[i][j - k + 1] >= k and l[i - k + 1][j] >= k:
                        maxLen = k

        return maxLen**2


grid = [[0, 0, 1], [1, 0, 1]]
print(Solution.largest1BorderedSquare(1, grid))
