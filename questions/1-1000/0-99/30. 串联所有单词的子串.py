# -*- coding: utf-8 -*-
# File:      30. 串联所有单词的子串.py
# DATA:      2022/6/23
# Software:  PyCharm
from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = []
        m, n, ls = len(words), len(words[0]), len(s)
        for i in range(n):
            if i + m * n > ls:
                break
            differ = Counter()
            for j in range(m):
                word = s[i + j * n:i + (j + 1) * n]
                differ[word] += 1
            print(differ)
            for word in words:
                differ[word] -= 1
                if differ[word] == 0:
                    del differ[word]
            for start in range(i, ls - m * n + 1, n):
                if start != i:
                    word = s[start + (m - 1) * n:start + m * n]
                    differ[word] += 1
                    if differ[word] == 0:
                        del differ[word]
                    word = s[start - n:start]
                    differ[word] -= 1
                    if differ[word] == 0:
                        del differ[word]
                if len(differ) == 0:
                    ans.append(start)
        return ans


print(Solution().findSubstring(s="barfoothefoobarman", words=["foo", "bar"]))
