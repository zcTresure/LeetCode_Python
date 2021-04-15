class Solution:
    def superPow(self, a: int, b: list) -> int:
        if len(b) == 0:
            return 1
        exp = b.pop()
        part1 = self.fastPow(a, exp)
        part2 = self.fastPow(self.superPow(a, b), 10)
        return (part1 * part2) % 1337

    def fastPow(self, a: int, exp: int) -> int:
        if exp == 0:
            return 1
        res = 1
        a %= 1337
        while exp:
            exp -= 1
            res *= a
        return res % 1337


a = 2
b = [1, 0]
test = Solution()
print(test.superPow(a, b))
