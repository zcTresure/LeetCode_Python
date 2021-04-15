class Solution:
    def tictactoe(self, moves: list) -> str:
        chess = [[0] * 3 for _ in range(3)]
        for i in range(len(moves)):
            x, y = moves[i]
            if i & 1:
                chess[x][y] = -1
            else:
                chess[x][y] = 1
        ans = set()
        for i in range(3):
            ans.add(sum(chess[i]))
            ans.add(sum(x[i] for x in chess))
        ans.add(sum(chess[i][i] for i in range(3)))
        ans.add(sum(chess[3 - i - 1][i] for i in range(3)))
        if 3 in ans:
            return "A"
        if -3 in ans:
            return "B"
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"


moves = [[0,0],[1,1]]
test = Solution()
print(test.tictactoe(moves))
