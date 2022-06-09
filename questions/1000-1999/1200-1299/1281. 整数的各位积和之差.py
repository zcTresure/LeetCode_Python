# -*- coding: utf-8 -*-
# File:      1281. 整数的各位积和之差.py
# DATA:      2022/6/8
# Software:  PyCharm
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul, add = 1, 0
        while n:
            digit = n % 10
            mul *= digit
            add += digit
            n //= 10
        return mul - add


print(Solution().subtractProductAndSum(n=234))
print(Solution().subtractProductAndSum(n=4421))
