# -*- coding: utf-8 -*-
# File:      419. 甲板上的战舰.py
# DATA:      2021/12/18
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    # 遍历扫描
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        m, n = len(board), len(board[0])
        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch == 'X':
                    row[j] = '.'
                    for k in range(j + 1, n):
                        if row[k] != 'X':
                            break
                        row[k] = '.'
                    for k in range(i + 1, m):
                        if board[k][j] != 'X':
                            break
                        board[k][j] = '.'
                    ans += 1
        return ans

    def countBattleships(self, board: List[List[str]]) -> int:
        return sum(ch == 'X' and not (i > 0 and board[i - 1][j] == 'X' or j > 0 and board[i][j - 1] == 'X')
                   for i, row in enumerate(board) for j, ch in enumerate(row))


board = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
print(Solution().countBattleships(board))
