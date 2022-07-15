# -*- coding: utf-8 -*-
# File:    745. 前缀和后缀搜索.py
# Date:    2022/7/15
# Software: Pycharm
from itertools import zip_longest
from typing import List


class WordFilter:

    def __init__(self, words: List[str]):
        self.d = {}
        for i, word in enumerate(words):
            m = len(word)
            for prefixLength in range(1, m + 1):
                for suffixLength in range(1, m + 1):
                    self.d[word[:prefixLength] + '#' + word[-suffixLength:]] = i

    def f(self, pref: str, suff: str) -> int:
        return self.d.get(pref + '#' + suff, -1)

    def __init__(self, words: List[str]):
        self.trie = {}
        self.weightKey = ('#', '#')
        for i, word in enumerate(words):
            cur = self.trie
            m = len(word)
            for j in range(m):
                tmp = cur
                for k in range(j, m):
                    key = (word[k], '#')
                    if key not in tmp:
                        tmp[key] = {}
                    tmp = tmp[key]
                    tmp[self.weightKey] = i
                tmp = cur
                for k in range(j, m):
                    key = ('#', word[-k - 1])
                    if key not in tmp:
                        tmp[key] = {}
                    tmp = tmp[key]
                    tmp[self.weightKey] = i
                key = (word[j], word[-j - 1])
                if key not in cur:
                    cur[key] = {}
                cur = cur[key]
                cur[self.weightKey] = i

    def f(self, pref: str, suff: str) -> int:
        cur = self.trie
        for key in zip_longest(pref, suff[::-1], fillvalue='#'):
            if key not in cur:
                return -1
            cur = cur[key]
        return cur[self.weightKey]
