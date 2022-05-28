# -*- coding: utf-8 -*-
# File:      面试题 17.11. 单词距离.py
# DATA:      2022/5/27
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        ans = len(words)
        index1, index2 = -1, -1
        for i, word in enumerate(words):
            if word == word1:
                index1 = i
            if word == word2:
                index2 = i
            if index1 > 0 and index2 > 0:
                ans = min(abs(index2 - index1), ans)
        return ans


words = ["I", "am", "a", "student", "from", "a", "university", "in", "a",
         "city"]
word1 = "am"
word2 = "from"
print(Solution().findClosest(words, word1, word2))
