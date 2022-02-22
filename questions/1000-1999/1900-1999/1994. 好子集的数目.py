# -*- coding: utf-8 -*-
# File:      1994. 好子集的数目.py
# DATA:      2022/2/22
# Software:  PyCharm
__author__ = 'zcFang'

from collections import Counter
from typing import List


class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]  # 30以内的质因数
        freq = Counter(nums)

        mod = 10 ** 9 + 7
        dp = [0] * (1 << len(primes))
        dp[0] = pow(2, freq[1], mod)
        for num, cnt in freq.items():
            if num == 1:  # 跳过乘积1
                continue

            # 检查 num 的质因数是否均不超过 1 个
            subset = 0
            check = False
            for i, prime in enumerate(primes):
                # num 相同的质因数超过一个
                if num % (prime * prime) == 0:
                    check = True
                    break

                if num % prime == 0:
                    # 记录质因数
                    subset |= (1 << i)
            if check:
                continue

            # 动态规划
            for mask in range((1 << len(primes))- 1, 0, -1):
                if (mask & subset) == subset:
                    dp[mask] = (dp[mask] + dp[mask ^ subset] * cnt) % mod  # 因为数组中含多个num，乘以cnt

        ans = sum(dp[1:]) % mod
        return ans


print(Solution().numberOfGoodSubsets(nums=[1, 2, 3, 4]))
print(Solution().numberOfGoodSubsets(nums=[4, 2, 3, 15]))
