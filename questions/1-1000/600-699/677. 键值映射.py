# -*- coding: utf-8 -*-
# File:      677. 键值映射.py
# DATA:      2021/9/24
# Software:  PyCharm
__author__ = 'zcFang'


class Trie:
    def __init__(self):
        self.child = dict()
        self.is_end = False
        self.val = 0

    def insert(self, word: str, val: int) -> None:
        root = self
        for c in word:
            if c not in root.child:
                root.child[c] = Trie()
            root = root.child[c]
        root.val = val
        root.is_end = True

    def searchAndGet(self, prefix: str) -> int:
        root = self
        for c in prefix:
            if c not in root.child:
                return 0
            root = root.child[c]
        return self.dfs(root)

    def dfs(self, root) -> int:
        if root == None:
            return 0
        res = root.val
        for ch in root.child.values():
            res += self.dfs(ch)
        return res


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.trie.insert(key, val)

    def sum(self, prefix: str) -> int:
        return self.trie.searchAndGet(prefix)
