# -*- coding: utf-8 -*-
# File:      676. 实现一个魔法字典.py
# DATA:      2021/9/24
# Software:  PyCharm
__author__ = 'zcFang'

from collections import defaultdict
from typing import List


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.buckets[len(word)].append(word)

    def search(self, searchWord: str) -> bool:
        return any(sum(a != b for a, b in zip(searchWord, candidate)) == 1
                   for candidate in self.buckets[len(searchWord)])

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
