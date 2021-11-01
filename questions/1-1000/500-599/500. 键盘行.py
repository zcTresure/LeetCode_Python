# -*- coding: utf-8 -*-
# File:      500. 键盘行.py
# DATA:      2021/11/1
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        rowIdx = "12210111011122000010020202"
        for word in words:
            idx = rowIdx[ord(word[0].lower()) - ord('a')]
            if all(rowIdx[ord(ch.lower()) - ord('a')] == idx for ch in word):
                ans.append(word)
        return ans


words = ["Hello", "Alaska", "Dad", "Peace"]
print(Solution().findWords(words))
