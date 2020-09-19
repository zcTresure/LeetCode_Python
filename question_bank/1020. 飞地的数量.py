import collections


class Solution:
    # 广度优先搜索
    def numEnclaves(self, A: list) -> int:
        if not A:
            return []
        m, n = len(A), len(A[0])
        q = collections.deque()
        land = set()
        for x in range(m):
            if A[x][0] == 1:
                land.add((x, 0))
                q.append((x, 0))
            if A[x][n - 1] == 1:
                land.add((x, n - 1))
                q.append((x, n - 1))
        for y in range(1, n - 1):
            if A[0][y] == 1:
                land.add((0, y))
                q.append((0, y))
            if A[m - 1][y] == 1:
                land.add((m - 1, y))
                q.append((m - 1, y))
        while q:
            x, y = q.popleft()
            A[x][y] = 2
            for r, c in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= r < m and 0 <= c < n and A[r][c] == 1 and (r, c) not in land:
                    q.append((r, c))
        ans = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    ans += 1
        return ans

    # 深度优先搜索
    # def numEnclaves(self, A: list) -> int:
    #     def dfs(x: int, y: int) -> None:
    #         if not 0 <= x < m or not 0 <= y < n or A[x][y] == 0 or (x, y) in land:
    #             return
    #         land.add((x, y))
    #         A[x][y] = 2
    #         for r, c in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
    #             dfs(r, c)
    #     if not A:
    #         return 0
    #     land = set()
    #     m, n = len(A), len(A[0])
    #     for x in range(m):
    #         dfs(x, 0)
    #         dfs(x, n - 1)
    #     for y in range(n):
    #         dfs(0, y)
    #         dfs(m - 1, y)
    #     ans = 0
    #     for i in range(m):
    #         for j in range(n):
    #             if A[i][j] == 1:
    #                 ans += 1
    #     return ans


A = [[0, 0, 0, 0],
     [1, 0, 1, 0],
     [0, 1, 1, 0],
     [0, 0, 0, 0]]
# A = [[0, 1, 1, 0],
#      [0, 0, 1, 0],
#      [0, 0, 1, 0],
#      [0, 0, 0, 0]]
test = Solution()
print(test.numEnclaves(A))
for i in range(len(A)):
    print(A[i])
