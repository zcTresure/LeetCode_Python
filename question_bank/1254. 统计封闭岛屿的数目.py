class Solution:
    def closedIsland(self, grid: list) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        def dfs(x: int, y: int):
            grid[x][y] = 1
            for rx, ry in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= rx < m and 0 <= ry < n and grid[rx][ry] == 0:
                    dfs(rx, ry)

        for x in range(m):
            if grid[x][0] == 0:
                dfs(x, 0)
            if grid[x][n - 1] == 0:
                dfs(x, n - 1)
        for y in range(n):
            if grid[0][y] == 0:
                dfs(0, y)
            if grid[m - 1][y] == 0:
                dfs(m - 1, y)
        for x in range(1, m - 1):
            for y in range(1, n - 1):
                if grid[x][y] == 0:
                    res += 1
                    dfs(x, y)
        return res


grid = [[1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]]
test = Solution()
print(test.closedIsland(grid))
