class Solution:
    def exist(self, board: list, word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def check(x: int, y: int, index: int) -> bool:
            if board[x][y] != word[index]:
                return False
            if index == len(word) - 1:
                return True
            visited.add((x, y))
            result = False
            for cx, cy in directions:
                newx, newy = cx + x, cy + y
                if (newx, newy) not in visited and 0 <= newx < len(board) and 0 <= newy < len(board[0]):
                    if check(newx, newy, index + 1):
                        result = True
                        break
            visited.remove((x, y))
            return result
        row, column = len(board), len(board[0])
        for x in range(row):
            for y in range(column):
                if check(x, y, 0):
                    return True
        return False
