# -*- coding: utf-8 -*-
# File:      953. 验证外星语词典.py
# DATA:      2022/5/17
# Software:  PyCharm
__author__ = 'zcFang'

from itertools import pairwise
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = {c: i for i, c in enumerate(order)}
        return all(s <= t for s, t in pairwise([index[c] for c in word] for word in words))


words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(Solution().isAlienSorted(words, order))
