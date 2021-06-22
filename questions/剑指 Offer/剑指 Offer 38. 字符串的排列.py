# -*- coding: utf-8 -*-
# File:     剑指 Offer 38. 字符串的排列.py
# Date:     2021/6/22
# Software: PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        s ,ans = list(s), []
        s.sort()
        n = len(s)
        visited = [False] * n

        def backtrack(prem: List[str], idx: int, n: int) -> None:
            if idx == n:
                ans.append("".join(prem))
                return
            for i in range(n):
                if visited[i] or (i > 0 and not visited[i - 1] and s[i - 1] == s[i]):
                    continue
                visited[i] = True
                prem.append(s[i])
                backtrack(prem, idx + 1, n)
                prem.pop()
                visited[i] = False

        backtrack([], 0, n)
        return ans


s = input("输入字符串:")
print(Solution().permutation(s))
