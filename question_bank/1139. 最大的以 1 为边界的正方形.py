class Solution:
    def largest1BorderedSquare(self, grid: list) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 or n == 1:
            return max(grid[0])
        row = [[0] * m for _ in range(n)]
        column = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row[i][j] = row[i][j - 1] + grid[i][j]
        for i in range(n):
            for j in range(m):
                if grid[j][i] == 1:
                    column[j][i] = column[j - 1][i] + grid[j][i]
        maxlen = 0
        for i in range(m):
            for j in range(n):
                if row[i][j] == column[i][j] and row[i][j] > maxlen:
                    maxlen = row[i][j]
        for i in range(m):
            print(row[i])
        for i in range(n):
            print(column[i])
        return maxlen * maxlen


grid = [[0, 0, 1], [1, 0, 1]]
print(Solution.largest1BorderedSquare(1, grid))
