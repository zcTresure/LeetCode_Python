# File Name:  263. 丑数
# date:       2021/4/10
# encode:      UTF-8
__author__ = 'zcTresure'


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0: return False
        factors = [2, 3, 5]
        for factor in factors:
            while n % factor == 0:
                n //= factor
        return n == 1


test = Solution()
while True:
    n = int(input("输入整数："))
    print(test.isUgly(n))