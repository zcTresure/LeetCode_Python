# -*- coding: utf-8 -*-
# File:      397. 整数替换.py
# DATA:      2021/11/19
# Software:  PyCharm
__author__ = 'zcFang'

from functools import cache


class Solution:
    # 贪心
    def integerReplacement(self, n: int) -> int:
        ans = 0
        while n != 1:
            if n % 2 == 0:
                ans += 1
                n //= 2
            elif n % 4 == 1:
                ans += 2
                n //= 2
            else:
                if n == 3:
                    ans += 2
                    n = 1
                else:
                    ans += 2
                    n = n // 2 + 1
        return ans

    # 递归
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 0:
            return 1 + self.integerReplacement(n // 2)
        return 2 + min(self.integerReplacement(n // 2), self.integerReplacement(n // 2 + 1))

    # 记忆化搜索
    @cache
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 0:
            return 1 + self.integerReplacement(n // 2)
        return 2 + min(self.integerReplacement(n // 2), self.integerReplacement(n // 2 + 1))


if __name__ == '__main__':
    while True:
        n = int(input('输入数字: '))
        print(Solution().integerReplacement(n))
