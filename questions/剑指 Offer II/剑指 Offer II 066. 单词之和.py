# -*- coding: utf-8 -*-
# File:      剑指 Offer II 066. 单词之和.py
# DATA:      2022/5/31
# Software:  PyCharm
__author__ = 'zcFang'


class TireNode:
    def __init__(self):
        self.val = 0
        self.next = [None for _ in range(26)]


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TireNode()
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        delta = val
        if key in self.map:
            delta -= self.map[key]
        self.map[key] = val
        node = self.root
        for c in key:
            if node.next[ord(c) - ord('a')] is None:
                node.next[ord(c) - ord('a')] = TireNode()
            node = node.next[ord(c) - ord('a')]
            node.val += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            if node.next[ord(c) - ord('a')] is None:
                return 0
            node = node.next[ord(c) - ord('a')]
        return node.val

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
