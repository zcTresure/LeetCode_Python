def climbStairs(self, n):
    if n == 1 or n == 2:  return 1
    x, y, res = 1, 2, 0
    for i in range(3, n + 1):
        res = x + y;
        x, y = y, res
    return res

print(climbStairs(2, 5))
