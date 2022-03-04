# -*- coding: utf-8 -*-
# File:      564. 寻找最近的回文数.py
# DATA:      2022/3/2
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        m = len(n)
        candidates = [10 ** (m - 1) - 1, 10 ** m + 1]
        self_prefix = int(n[:(m + 1) // 2])
        for x in range(self_prefix - 1, self_prefix + 2):
            y = x if m % 2 == 0 else x // 10
            while y:
                x = x * 10 + y % 10
                y //= 10
            candidates.append(x)
        ans = -1
        self_num = int(n)
        for candidate in candidates:
            if candidate != self_num:
                if ans == -1 or abs(candidate - self_num) < abs(ans - self_num) or \
                        abs(candidate - self_num) == abs(ans - self_num) and candidate < ans:
                    ans = candidate
        return str(ans)


print(Solution().nearestPalindromic(n='123'))
