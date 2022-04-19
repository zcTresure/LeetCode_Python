# -*- coding: utf-8 -*-
# File:      386. 字典序排数.py
# DATA:      2022/4/18
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [0] * n
        num = 1
        for i in range(n):
            ans[i] = num
            if num * 10 <= n:
                num *= 10
            else:
                while num % 10 == 9 or num + 1 > n:
                    num //= 10
                num += 1
        return ans

print(Solution().lexicalOrder(n=50))

