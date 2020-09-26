class NumMatrix:
    # 暴力
    def __init__(self, matrix: list):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for r in range(row1, row2 + 1):
            for c in range(col1, col2 + 1):
                ans += self.matrix[r][c]
        return ans

    # 动态规划缓存每一行
    def __init__(self, matrix: list):
        self.dp = [[0] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.dp[i].append(self.dp[i][-1] + matrix[i][j])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for r in range(row1, row2 + 1):
            ans += self.dp[r][col2 + 1] - self.dp[r][col1]
        return ans

    # 动态规划缓存整个数组
    def __init__(self, matrix: list):
        if not matrix:
            return
        self.dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.dp[i + 1][j + 1] = self.dp[i + 1][j] + \
                    self.dp[i][j + 1] + matrix[i][j] - self.dp[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] - self.dp[row2 + 1][col1] - self.dp[row1][col2 + 1] + self.dp[row1][col1]


matrix = [[3, 0, 1, 4, 2],
          [5, 6, 3, 2, 1],
          [1, 2, 0, 1, 5],
          [4, 1, 0, 1, 7],
          [1, 0, 3, 0, 5]]
test = NumMatrix(matrix)
print(test.sumRegion(2, 1, 4, 3))

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
