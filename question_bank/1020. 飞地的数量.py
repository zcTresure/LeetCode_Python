import collections


class Solution:
    # 广度优先搜索
    def numEnclaves(self, A: list) -> int:
        if A == []: return 0
        row, col = len(A), len(A[0])
        boundary = set()
        for i in range(row):
            if A[i][0] == 1:
                boundary.add((i, 0))
            if A[i][col - 1] == 1:
                boundary.add((i, col - 1))
        for j in range(col):
            if A[0][j] == 1:
                boundary.add((0, j))
            if A[row - 1][j] == 1:
                boundary.add((row - 1, j))
        queue = collections.deque(boundary)
        while queue:
            x, y = queue.popleft()
            A[x][y] = 0
            for xi, yi in [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= xi < row and 0 <= yi < col and (xi, yi) not in boundary and A[xi][yi] == 1:
                    queue.append((xi, yi))
                    boundary.add((xi, yi))
        return sum(sum(A[i]) for i in range(row))


    # 深度优先搜索
    def numEnclaves(self, A: list) -> int:
        def dfs(x: int, y: int) -> None:
            if not 0 <= x < m or not 0 <= y < n or A[x][y] == 0 or (x, y) in land:
                return
            land.add((x, y))
            A[x][y] = 0
            for r, c in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                dfs(r, c)
        if not A:
            return 0
        land = set()
        m, n = len(A), len(A[0])
        for x in range(m):
            dfs(x, 0)
            dfs(x, n - 1)
        for y in range(n):
            dfs(0, y)
            dfs(m - 1, y)
        return sum(sum(A[i]) for i in range(m))


A = [[0, 0, 0, 0],
     [1, 0, 1, 0],
     [0, 1, 1, 0],
     [0, 0, 0, 0]]
A = [[0, 1, 1, 0],
     [0, 0, 1, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 0]]
test = Solution()
print(test.numEnclaves(A))
for i in range(len(A)):
    print(A[i])
