# -*- coding: utf-8 -*-
# File:      212. 单词搜索 II.py
# DATA:      2021/9/16
# Software:  PyCharm
__author__ = 'zcFang'

from collections import defaultdict
from typing import List


class Tire:
    def __init__(self):
        self.children = defaultdict(Tire)
        self.word = ""

    def insert(self, word: str):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.is_word = True
        cur.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tire = Tire()
        for word in words:
            tire.insert(word)

        def dfs(now, row, col):
            if board[row][col] not in now.children:
                return
            ch = board[row][col]
            now = now.children[ch]
            if now.word != "":
                ans.add(now.word)
            board[row][col] = "#"
            for now_row, now_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if 0 <= now_row < len(board) and 0 <= now_col < len(board[0]):
                    dfs(now, now_row, now_col)
            board[row][col] = ch

        ans = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(tire, row, col)
        return list(ans)

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tire = Tire()
        for word in words:
            tire.insert(word)

        def dfs(now, row, col):
            if board[row][col] not in now.children:
                return
            ch = board[row][col]
            next = now.children[ch]
            if next.word != "":
                ans.add(next.word)
                next.word = ""
            if next.children:
                board[row][col] = "#"
                for next_row, next_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                    if 0 <= next_row < len(board) and 0 <= next_col < len(board[0]):
                        dfs(next, next_row, next_col)
                board[row][col] = ch

        ans = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(tire, row, col)
        return list(ans)
