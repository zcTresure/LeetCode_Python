class Solution:
    def exist(self, board: list, word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(i, j, k):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            tmp, board[i][j] = board[i][j], '.'
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k +
                                              1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = tmp
            return res
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(Solution.exist(1, board, word))
