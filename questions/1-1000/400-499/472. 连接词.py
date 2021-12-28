# -*- coding: utf-8 -*-
# File:      472. 连接词.py
# DATA:      2021/9/23
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word: str):
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def dfs(self, word: str, start: int, vis: List[bool]) -> bool:
        if start == len(word):
            return True
        if vis[start]:
            return False
        vis[start] = True
        node = self
        for i in range(start, len(word)):
            node = node.children[ord(word[i]) - ord('a')]
            if node is None:
                return False
            if node.isEnd and self.dfs(word, i + 1, vis):
                return True
        return False


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)

        ans = []
        root = Trie()
        for word in words:
            if word == "":
                continue
            if root.dfs(word, 0, [False] * len(word)):
                ans.append(word)
            else:
                root.insert(word)
        return ans


words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
print(Solution().findAllConcatenatedWordsInADict(words))
