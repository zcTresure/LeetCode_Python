# File Name:  633. 平方数之和
# date:       2021/4/28
# encode:      UTF-8

from math import sqrt


class Solution:
    # 使用sqrt函数
    def judgeSquareSum(self, c: int) -> bool:
        target = int(sqrt(c) + 1)
        for i in range(target):
            if sqrt(c - i * i) == int(sqrt(c - i * i)):
                return True
        return False

    # 双指针
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(sqrt(c))
        while left <= right:
            tmp = left * left + right * right
            if tmp == c:
                return True
            elif tmp < c:
                left += 1
            else:
                right -= 1
        return False

    # 数学
    def judgeSquareSum(self, c: int) -> bool:
        for base in range(2, int(sqrt(c))):
            if c % base != 0:
                continue
            exp = 0
            while c % base == 0:
                c //= base
                exp += 1
            if (base % 4 == 3 and exp % 2 != 0):
                return False
        return c % 4 != 3


print(Solution().judgeSquareSum(5))
print(Solution().judgeSquareSum(2))
print(Solution().judgeSquareSum(3))
