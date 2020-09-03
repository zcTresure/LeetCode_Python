# 深度优先搜索
class Solution:
    def updateBoard(self, board: list, click: list) -> list:
        n, m = len(board), len(board[0])
        dic = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
               (0, 1), (1, -1), (1, 0), (1, 1)]

        def dfs(x: int, y: int) -> None:
            if board[x][y] == 'M':
                board[x][y] = 'X'
                return
            cnt = 0
            for mx, my in dic:
                mx, my = x + mx, y + my
                if 0 <= mx < n and 0 <= my < m:
                    cnt += 1 if board[mx][my] == 'M' else 0
            if cnt != 0:
                board[x][y] = str(cnt)
            else:
                board[x][y] = 'B'
                for mx, my in dic:
                    mx, my = x + mx, y + my
                    if 0 <= mx < n and 0 <= my < m and board[mx][my] == 'E':
                        dfs(mx, my)

        dfs(click[0], click[1])
        return board


class Solution:
    def updateBoard(self, board: list, click: list) -> list:
        n, m = len(board), len(board[0])
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]

        def dfs(board: list, x: int, y: int) -> None:
            if board[x][y] == 'M':
                board[x][y] = 'X'
                return
            cnt = 0
            for i in range(8):
                mx, my = x + dx[i], y + dy[i]
                if 0 <= mx < n and 0 <= my < m:
                    cnt += 1 if board[mx][my] == 'M' else 0
            if cnt != 0:
                board[x][y] = str(cnt)
            else:
                board[x][y] = 'B'
                for i in range(8):
                    mx, my = x + dx[i], y + dy[i]
                    if mx < 0 or mx >= n or my < 0 or my >= m or board[mx][my] != 'E':
                        continue
                    dfs(board, mx, my)

        dfs(board, click[0], click[1])
        return board


from collections import deque


class Solution:
    def updateBoard(self, board: list, click: list) -> list:
        n, m = len(board), len(board[0])
        dic = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
               (0, 1), (1, -1), (1, 0), (1, 1)]

        def bfs(sx: int, sy: int):
            queue = deque()
            visit = [[False] * m for _ in range(n)]
            queue.append((sx, sy))
            visit[sx][sy] = True
            while queue:
                cnt = 0
                x, y = queue.popleft()
                for mx, my in dic:
                    mx, my = mx + x, my + y
                    if 0 <= mx < n and 0 <= my < m:
                        cnt += 1 if board[mx][my] == 'M' else 0
                if cnt != 0:
                    board[x][y] = str(cnt)
                else:
                    board[x][y] = 'B'
                    for mx, my in dic:
                        mx, my = mx + x, my + y
                        if 0 <= mx < n and 0 <= my < m and board[mx][my] == 'E' and visit[mx][my] == False:
                            queue.append((mx, my))
                            visit[mx][my] = True
        x, y = click[0], click[1]
        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            bfs(x, y)
        return board


board = [["B", "1", "E", "1", "B"], ["B", "1", "M", "1", "B"],
         ["B", "1", "1", "1", "B"], ["B", "B", "B", "B", "B"]]

click = [1, 2]
test = Solution()
ans = test.updateBoard(board, click)
for i in range(len(ans)):
    print(ans[i])
