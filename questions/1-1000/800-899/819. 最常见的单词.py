# -*- coding: utf-8 -*-
# File:      819. 最常见的单词.py
# DATA:      2022/4/17
# Software:  PyCharm
__author__ = 'zcFang'

from collections import Counter
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        freq = Counter()
        banned = set(banned)
        word, n = "", len(paragraph)
        for i in range(n + 1):
            if i < n and paragraph[i].isalpha():
                word += paragraph[i].lower()
            elif word:
                if word not in banned:
                    freq[word] += 1
                word = ""
        max_freq = max(freq.values())
        return next(word for word, f in freq.items() if f == max_freq)


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(Solution().mostCommonWord(paragraph, banned))
