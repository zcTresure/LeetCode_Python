# -*- coding: utf-8 -*-
# File:      720. 词典中最长的单词.py
# DATA:      2021/9/25
# Software:  PyCharm
__author__ = 'zcFang'

from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self):
        self.end = False
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for s in word:
            node = node.children[s]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for s in word:
            node = node.children.get(s)
            if node is None or not node.end:
                return False
        return True


class Solution:
    # 哈希表
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        dic, ans = set(), ""
        for word in words:
            if len(word) == 1 or word[:-1] in dic:
                dic.add(word)
                ans = word if len(word) > len(ans) else ans
        return ans

    # 前缀树
    def longestWord(self, words: List[str]) -> str:
        res = ''
        trie = Trie()
        for word in words:
            trie.insert(word)
        for word in words:
            if trie.search(word):
                if len(word) > len(res):
                    res = word
                elif len(word) == len(res) and word < res:
                    res = word
        return res


# words = ["w", "wo", "wor", "worl", "world"]
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
print(Solution().longestWord(words))
