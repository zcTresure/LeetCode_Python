# -*- coding: utf-8 -*-
# File:      762. 二进制表示中质数个计算置位.py
# DATA:      2022/4/5
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        for num in range(left, right + 1):
            cnt = bin(num).count('1')
            if cnt in primes:
                ans += 1
        return ans

    def countPrimeSetBits(self, left: int, right: int) -> int:
        return sum(((1 << x.bit_count()) & 665772) != 0 for x in range(left, right + 1))


print(Solution().countPrimeSetBits(left=6, right=10))
print(Solution().countPrimeSetBits(left=10, right=15))
