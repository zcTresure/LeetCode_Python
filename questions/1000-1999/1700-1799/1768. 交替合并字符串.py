# -*- coding: utf-8 -*-
# File:      1768. 交替合并字符串.py
# DATA:      2022/6/15
# Software:  PyCharm
from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        i, j = 0, 0
        ans = ''
        while i < m and j < n:
            ans = ans + word1[i] + word2[j]
            i += 1
            j += 1
        # if i < m:
        ans = ans + word1[i:m]
        # if j < n:
        ans = ans + word2[j:n]
        return ans


print(Solution().mergeAlternately(word1="abc", word2="pqr"))
print(Solution().mergeAlternately(word1="ab", word2="pqrs"))
print(Solution().mergeAlternately(word1="abcd", word2="pq"))
