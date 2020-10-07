class Solution:
    def tictactoe(self, board: list) -> str:
        N = len(board)
        if ('X' * N) in board:
            return 'X'
        if 'O' * N in board:
            return 'O'
        x = ['X'] * N
        o = ['O'] * N

        def judgement(arr):
            if arr == x or arr == o:
                return True
            return False
        # 判断每一列
        for i in range(N):
            temp = [j[i] for j in board]
            if judgement(temp):
                return temp[0]
        # 判断对角线
        temp1, temp2 = [], []
        for i in range(N):
            temp1.append(board[i][i])
            temp2.append(board[i][N - 1 - i])
        if judgement(temp1):
            return temp1[0]
        if judgement(temp2):
            return temp2[0]
        for i in board:
            if ' ' in i:
                return "Pending"
        return "Draw"


board = ["O X", " XO", "X O"]
test = Solution()
print(test.tictactoe(board))
