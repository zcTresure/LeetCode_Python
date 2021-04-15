class Solution:
    # 基于集合的回溯 时间N!
    def solveNQueens(self, n: int) -> list:
        solution = list()
        # 每一行皇后所在的位置
        queens = [-1] * n
        # 标记每一列的皇后
        colums = set()
        # 标记与主对角线平行的皇后
        diagonal1 = set()
        # 标记与副对角线平行的皇后
        diagonal2 = set()
        # 棋盘每行初始状态
        row = ['.'] * n

        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = 'Q'
                board.append(''.join(row))
                row[queens[i]] = '.'
            return board

        def backtrack(row: int):
            if row == n:
                board = generateBoard()
                solution.append(board)
            else:
                for i in range(n):
                    if i in colums or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    # 记录第i个皇后的地址
                    queens[row] = i
                    # 记录皇后的列、主对角线、副对角线
                    colums.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    # 移除皇后的列、主对角线、副对角线
                    colums.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)
        backtrack(0)
        return solution

    # 基于位运算的回溯 N!
    def solveNQueens(self, n: int) -> list:
        solution = list()
        queens = [-1] * n
        row = ['.'] * n

        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = 'Q'
                board.append(''.join(row))
                row[queens[i]] = '.'
            return board

        def solve(row: int, columns: int, diagonals1: int, diagonals2: int):
            if row == n:
                board = generateBoard()
                solution.append(board)
            else:
                availablePositions = (
                    (1 << n) - 1) & (~(columns | diagonals1 | diagonals2))
                while availablePositions:
                    position = availablePositions & (-availablePositions)
                    availablePositions = availablePositions & (
                        availablePositions - 1)
                    column = bin(position - 1).count("1")
                    queens[row] = column
                    solve(row + 1, columns | position, (diagonals1 |
                                                        position) << 1, (diagonals2 | position) >> 1)
        solve(0, 0, 0, 0)
        return solution


test = Solution()
n = 1
while n:
    n = int(input('input:'))
    ans = test.solveNQueens(n)
    for i in range(len(ans)):
        print(ans[i])
