class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return 1
        x, y, res = 1, 2, 0
        for i in range(3, n + 1):
            res = x + y
            x, y = y, res
        return res

    def climbStairs(self, n: int) -> int:
        a, b, c = 1, 1, 1
        for i in range(2, n + 1):
            c = a + b
            b, a, = c, b
        return c


while 1:
    n = int(input('input:'))
    test = Solution()
    print(test.climbStairs(n))
