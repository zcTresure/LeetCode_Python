# -*- coding: utf-8 -*-
# File:      318. 最大单词长度乘积.py
# DATA:      2021/11/17
# Software:  PyCharm
__author__ = 'zcFang'

from collections import defaultdict
from functools import reduce
from itertools import product
from typing import List


class Solution:
    # 位运算
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0] * n

        for i in range(n):
            word = words[i]
            for j in range(len(word)):
                masks[i] |= (1 << (ord(word[j]) - ord('a')))

        maxProd = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (masks[i] & masks[j] == 0):
                    maxProd = max(maxProd, len(words[i]) * len(words[j]))
        return maxProd

    def maxProduct(self, words: List[str]) -> int:
        masks = defaultdict(int)
        for word in words:
            mask = reduce(lambda a, b: a | (1 << (ord(b) - ord('a'))), word, 0)
            masks[mask] = max(masks[mask], len(word))
        return max((masks[x] * masks[y] for x, y in product(masks, repeat=2) if x & y == 0), default=0)


words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
print(Solution().maxProduct(words))
