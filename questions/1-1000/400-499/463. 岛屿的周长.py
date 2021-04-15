class Solution:
    def islandPerimeter(self, grid: list) -> int:
        def dfs(x: int, y: int):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return 1
            if grid[x][y] == 2:
                return 0
            grid[x][y] = 2
            res = 0
            for r, c in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                res += dfs(r, c)
            return res

        ans = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += dfs(i, j)
        return ans


grid = [[0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]]
test = Solution()
print(test.islandPerimeter(grid))
