import collections


# 深度优先搜索
class Solution:
    def solve(self, board: list) -> None:
        if not board:
            return
        n, m = len(board), len(board[0])

        def dfs(x: int, y: int):
            if not 0 <= x < n or not 0 <= y < m or board[x][y] != 'O':
                return
            board[x][y] = 'T'
            for r, c in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                dfs(r, c)
        for x in range(n):
            dfs(x, 0)
            dfs(x, m - 1)
        for y in range(m):
            dfs(0, y)
            dfs(n - 1, y)
        for x in range(n):
            for y in range(m):
                if board[x][y] == 'T':
                    board[x][y] = 'O'
                elif board[x][y] == 'O':
                    board[x][y] = 'X'


# 广度优先搜索
class Solution:
    def solve(self, board: list) -> None:
        if not board:
            return
        n, m = len(board), len(board[0])
        q = collections.deque()
        for x in range(n):
            if board[x][0] == 'O':
                q.append((x, 0))
            if board[x][m - 1] == 'O':
                q.append((x, m - 1))
        for y in range(m - 1):
            if board[0][y] == 'O':
                q.append((0, y))
            if board[n - 1][y] == 'O':
                q.append((n - 1, y))
        while q:
            x, y = q.popleft()
            board[x][y] = 'T'
            for r, c in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= r < n and 0 <= c < m and board[r][c] == "O":
                    q.append((r, c))
        for x in range(n):
            for y in range(m):
                if board[x][y] == 'T':
                    board[x][y] = 'O'
                elif board[x][y] == 'O':
                    board[x][y] = 'X'


board = [['X', 'X', 'X', 'X'],
         ['X', 'O', 'O', 'X'],
         ['X', 'X', 'O', 'X'],
         ['X', 'O', 'X', 'X']]
solution = Solution()
solution.solve(board)
for i in range(len(board)):
    print(board[i])
