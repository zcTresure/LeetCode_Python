class Solutions():
    # 暴力枚举
    def countNegatives(self, grid: list) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    ans += 1
        return ans

    # 二分查找
    def countNegatives(self, grid: list) -> int:
        m, n = len(grid[0]), len(grid)
        res, ind = 0, m
        for i in range(n):
            if ind == 0:
                break
            if grid[i][ind - 1] >= 0:
                continue
            left, right = 0, ind
            while left < right:
                mid = left + (right - left) // 2
                if grid[i][mid] >= 0:
                    left = mid + 1
                else:
                    right = mid
            res += (ind - left) * (n - i)
            ind = left
        return res


grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
test = Solutions()
print(test.countNegatives(grid))
