class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b, p, x, rem = n // 3 - 1, n % 3, 1000000007, 3, 1
        while a > 0:
            if a % 2: rem = (rem * x) % p
            x = x ** 2 % p
            a //= 2
        if b == 0:
            return (rem * 3) % p
        if b == 1:
            return (rem * 4) % p
        return (rem * 6) % p

    def cuttingRope(self, n: int) -> int:
        a, b, p = n // 3, n % 3, 10000000007
        if b == 0:
            return (3 ** a) % p
        elif b == 1:
            return (3 ** (a - 1) * 4) % p
        else:
            return (3 ** a * 2) % p


test = Solution()
print(test.cuttingRope(14))
