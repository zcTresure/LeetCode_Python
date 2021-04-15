class Solution:
    def fib(self, N: int) -> int:
        if N <= 0:
            return 0
        a, b, c = 1, 1, 1
        for i in range(3, N + 1):
            c = a + b
            b, a = c, b
        return c


N = 7
test = Solution()
print(test.fib(N))
