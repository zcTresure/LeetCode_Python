from collections import deque


class Solution:
    # 广度优先搜索
    def updateMatrix(self, matrix: list) -> list:
        m, n = len(matrix), len(matrix[0])
        dist = [[0] * n for _ in range(m)]
        zeros = [(i, j)for i in range(m)
                 for j in range(n) if matrix[i][j] == 0]
        seen = set(zeros)
        q = deque(zeros)
        while q:
            i, j = q.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
                    seen.add((ni, nj))
        return dist

    # 动态规划
    def updateMatrix(self, matrix: list) -> list:
        m, n = len(matrix), len(matrix[0])
        # 开始将所有的值设为最大值
        dist = [[float('inf')] * n for _ in range(m)]
        # 将所有的0值赋值
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
        # 水平向左移动 和 竖直向上移动
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
         # 水平向右移动 和 竖直向下移动
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + 1 < m:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j + 1 < n:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        return dist


matrix = [[0, 0, 0],
          [0, 1, 0],
          [1, 1, 1]]
res = Solution().updateMatrix(matrix)
for i in range(len(res)):
    print(res[i])
