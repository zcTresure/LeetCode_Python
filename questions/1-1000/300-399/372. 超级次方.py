from typing import List


class Solution:
    MOD = 1337

    def superPow(self, a: int, b: List[int]) -> int:
        def quickPow(a: int, exp: int) -> int:
            if exp == 0:
                return 1
            res = 1
            a %= 1337
            while exp:
                exp -= 1
                res *= a
            return res % self.MOD

        if len(b) == 0:
            return 1
        exp = b.pop()
        part1 = quickPow(a, exp)
        part2 = quickPow(self.superPow(a, b), 10)
        return (part1 * part2) % self.MOD

    def superPow(self, a: int, b: list) -> int:
        def dfs(a: int, b: List[int], i: int):
            if (i == -1): return 1
            return quickPow(dfs(a, b, i - 1), 10) * quickPow(a, b[i]) % self.MOD

        def quickPow(a: int, b: int):
            ans = 1
            a %= self.MOD
            while b:
                if b & 1:
                    ans = ans * a % self.MOD
                a = a * a % self.MOD
                b >>= 1
            return ans

        return dfs(a, b, len(b) - 1)


a = 2
b = [1, 0]
test = Solution()
print(test.superPow(a, b))
