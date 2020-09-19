# 深度优先搜索 结果超出时间限制
class Solution:
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def longestIncreasingPath(self, matrix: list) -> int:
        if not matrix:
            return 0
        rows, columns = len(matrix), len(matrix[0])
        ans = 0

        def dfs(row: int, column: int) -> int:
            up = 1
            for dx, dy in Solution.DIRS:
                newRow, newColumn = row + dx, column + dy
                if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > matrix[row][column]:
                    up = max(up, dfs(newRow, newColumn) + 1)
            return up
        for i in range(rows):
            for j in range(columns):
                ans = max(ans, dfs(i, j))
        return ans

    # 拓扑排序
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def longestIncreasingPath(self, matrix: list) -> int:
        if not matrix:
            return 0
        rows, columns = len(matrix), len(matrix[0])
        outdegrees = [[0] * columns for _ in range(rows)]
        queue = collections.deque()
        for i in range(rows):
            for j in range(columns):
                for dx, dy in Solution.DIRS:
                    newRow, newColumn = i + dx, j + dy
                    if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > matrix[i][j]:
                        outdegrees[i][j] += 1
                if outdegrees[i][j] == 0:
                    queue.append((i, j))
        ans = 0
        while queue:
            ans += 1
            size = len(queue)
            for _ in range(size):
                row, column = queue.popleft()
                for dx, dy in Solution.DIRS:
                    newRow, newColumn = row + dx, column + dy
                    if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] < matrix[row][column]:
                        outdegrees[newRow][newColumn] -= 1
                        if outdegrees[newRow][newColumn] == 0:
                            queue.append((newRow, newColumn))
        return ans

    # 记忆化+深度优先搜索
    def longestIncreasingPath(self, matrix: list) -> int:
        if not matrix:
            return 0
        nxt = ((1, 0), (-1, 0), (0, -1), (0, 1))
        old = {}
        matrix = [[float("inf")] + i + [float("inf")] for i in matrix]
        col = len(matrix[0])
        matrix = [[float("inf")] * col] + matrix + [[float("inf")] * col]
        row = len(matrix)

        def maxIncreasingRoute(x: int, y: int) -> int:
            if (x, y) in old:
                return old[(x, y)]
            if x in {0, row - 1} or y in {0, col - 1}:
                return 0
            old[(x, y)] = 1 + max([0] + [maxIncreasingRoute(x + xx, y + yy)
                                         for xx, yy in nxt if matrix[x][y] < matrix[x + xx][y + yy]])
            return old[(x, y)]
        return max([maxIncreasingRoute(i, j) for j in range(1, col - 1) for i in range(1, row - 1)])

    # 排序+动态规划
    def longestIncreasingPath(self, matrix: list) -> int:
        if not matrix:
            return 0
        x = len(matrix)
        y = len(matrix[0])
        dp = [[1 for _ in range(y)] for _ in range(x)]
        numsSort = sorted(sum([[(matrix[i][j], i, j)
                                for j in range(y)] for i in range(x)], []))
        for i, j, k in numsSort:
            dp[j][k] = 1 + max(
                dp[j - 1][k] if j and matrix[j - 1][k] < i else 0,
                dp[j][k - 1] if k and matrix[j][k - 1] < i else 0,
                dp[j + 1][k] if j != x - 1 and matrix[j + 1][k] < i else 0,
                dp[j][k + 1] if k != y - 1 and matrix[j][k + 1] < i else 0
            )
        return max(sum(dp, []))


nums = [
    [3, 4, 5],
    [3, 2, 6],
    [2, 2, 1]
]
test = Solution()
print(test.longestIncreasingPath(nums))
