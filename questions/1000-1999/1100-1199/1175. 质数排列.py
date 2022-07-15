# -*- coding: utf-8 -*-
# File:    1175. 质数排列.py
# Date:    2022/7/1
# Software: Pycharm
from math import sqrt


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes = sum(self.isPrime(i) for i in range(1, n + 1))
        return self.factorial(primes) * self.factorial(n - primes) % (10 ** 9 + 7)

    def isPrime(self, n: int) -> int:
        if n == 1:
            return 0
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return 0
        return 1

    def factorial(self, n: int) -> int:
        ans = 1
        for i in range(1, n + 1):
            ans *= i
            ans %= (10 ** 9 + 7)
        return ans


print(Solution().numPrimeArrangements(n=5))
print(Solution().numPrimeArrangements(n=100))
