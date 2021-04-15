class Solution:
    def shiftGrid(self, grid: list, k: int) -> list:
        m, n = len(grid), len(grid[0])
        new_grid = [[0] * n for _ in range(m)]
        for row in range(m):
            for col in range(n):
                new_row = ((row * n + col + k) // n) % m
                new_col = (k + col) % n
                new_grid[new_row][new_col] = grid[row][col]
        return new_grid


grid = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
k = 4
test = Solution()
print(test.shiftGrid(grid, k))
