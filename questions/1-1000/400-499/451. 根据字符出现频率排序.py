# -*- coding: utf-8 -*-
# File:      451. 根据字符出现频率排序.py
# DATA:      2021/7/3
# Software:  PyCharm
__author__ = 'zcFang'

from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        return ''.join(val * freq[val] for val in sorted(freq.keys(), key=lambda c: -freq[c]))


s = "tree"
print(Solution().frequencySort(s))
