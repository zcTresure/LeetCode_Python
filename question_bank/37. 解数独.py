class Solution:
    # 直接递归
    def solveSudoku(self, board: list) -> None:
        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
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
                if valid:
                    return

        row = [[False] * 9 for _ in range(9)]
        column = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _a in range(3)] for _b in range(3)]
        valid = False
        spaces = list()
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    row[i][digit] = column[j][digit] = block[i //
                                                             3][j // 3][digit] = True
        dfs(0)

    def solveSudoku(self, board: list) -> None:
        def flip(i: int, j: int, digit: int):
            row[i] ^= (1 << digit)
            column[j] ^= (1 << digit)
            block[i // 3][j // 3] ^= (1 << digit)

        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return
            i, j = spaces[pos]
            mask = ~(row[i] | column[j] | block[i // 3][j // 3]) & 0x1ff
            print(mask)
            while mask:
                digitMask = mask & (-mask)
                digit = bin(digitMask).count("0") - 1
                flip(i, j, digit)
                board[i][j] = str(digit + 1)
                dfs(pos + 1)
                flip(i, j, digit)
                mask &= (mask - 1)
                if valid:
                    return

        row = [0] * 9
        column = [0] * 9
        block = [[0] * 3 for _ in range(3)]
        valid = False
        spaces = list()
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    flip(i, j, digit)
        dfs(0)
        
    def solveSudoku(self, board: List[List[str]]) -> None:
        def flip(i: int, j: int, digit: int):
            line[i] ^= (1 << digit)
            column[j] ^= (1 << digit)
            block[i // 3][j // 3] ^= (1 << digit)
        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return
            i, j = spaces[pos]
            mask = ~(line[i] | column[j] | block[i // 3][j // 3]) & 0x1ff
            while mask:
                digitMask = mask & (-mask)
                digit = bin(digitMask).count("0") - 1
                flip(i, j, digit)
                board[i][j] = str(digit + 1)
                dfs(pos + 1)
                flip(i, j, digit)
                mask &= (mask - 1)
                if valid:
                    return
        line = [0] * 9
        column = [0] * 9
        block = [[0] * 3 for _ in range(3)]
        valid = False
        spaces = list()
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    digit = int(board[i][j]) - 1
                    flip(i, j, digit)
        while True:
            modified = False
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        mask = ~(line[i] | column[j] | block[i // 3][j // 3]) & 0x1ff
                        if not (mask & (mask - 1)):
                            digit = bin(mask).count("0") - 1
                            flip(i, j, digit)
                            board[i][j] = str(digit + 1)
                            modified = True
            if not modified:
                break
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    spaces.append((i, j))

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
