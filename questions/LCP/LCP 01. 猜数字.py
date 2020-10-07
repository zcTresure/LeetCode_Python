class Solution:
    def game(self, guess: list, answer: list) -> int:
        ans = 0
        for i in range(len(guess)):
            if guess[i] == answer[i]:
                ans += 1
        return ans

    def game(self, guess: list, answer: list) -> int:
        return sum([guess[i] == answer[i] for i in range(len(guess))])


guess = [1, 2, 3]
answer = [1, 2, 3]
test = Solution()
print(test.game(guess, answer))
