class Solution:
    # 直接递归
    def solveSudoku(self, board: list) -> None:
        def dfs(pos: int):
            # nonlocal valid
            if pos == len(spaces):
                # valid = True
                return
            i, j = spaces[pos]
            for digit in range(9):
                if row[i][digit] == column[j][digit] == block[i // 3][j // 3][digit] == False:
                    row[i][digit] = column[j][digit] = block[i //
                                                             3][j // 3][digit] = True
                    board[i][j] = str(digit + 1)
                    dfs(pos + 1)
                    row[i][digit] = column[j][digit] = block[i //
                                                             3][j // 3][digit] = False
                # if valid:
                #     return
        
        row = [[False] * 9 for _ in range(9)]
        column = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _a in range(3)] for _b in range(3)]
        spaces = list()
        # valid = False
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    row[i][digit] = column[j][digit] = block[i //
                                                             3][j // 3][digit] = True
        dfs(0)


board = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
         ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
         ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
         ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
         ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
         ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
         ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
         ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
         ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
Solution().solveSudoku(board)
for i in range(len(board)):
    print(board[i])
