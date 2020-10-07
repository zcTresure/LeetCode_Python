class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        for move in moves:
            if move == 'U': x += 1
            elif move == 'D': x -= 1
            elif move == 'L': y -= 1
            else: y += 1
        return x == 0 and y == 0


moves = "UDLL"
test = Solution()
print(test.judgeCircle(moves))
