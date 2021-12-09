# -*- coding: utf-8 -*-
# File:      794. 有效的井字游戏.py
# DATA:      2021/12/9
# Software:  PyCharm
__author__ = 'zcFang'

from collections import Counter
from typing import List


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:

        x_cnt = sum(row.count('X') for row in board)
        o_cnt = sum(row.count('O') for row in board)
        print(x_cnt, o_cnt)
        if x_cnt != o_cnt and o_cnt != x_cnt - 1:
            return False
        if self.win(board, 'X') and o_cnt != x_cnt - 1:
            return False
        if self.win(board, 'O') and o_cnt != x_cnt:
            return False
        return True

    def win(self, board: List[str], c: chr) -> bool:
        for i in range(3):
            if c == board[i][0] and c == board[i][1] and c == board[i][2]:
                return True
            if c == board[0][i] and c == board[1][i] and c == board[2][i]:
                return True
        if c == board[0][0] and c == board[1][1] and c == board[2][2]:
            return True
        if c == board[0][2] and c == board[1][1] and c == board[2][0]:
            return True
        return False

    def win(self, board: List[str], c: chr) -> bool:
        return any(board[i][0] == c and board[i][1] == c and board[i][2] == c or
                   board[0][i] == c and board[1][i] == c and board[2][i] == c for i in range(3)) or \
               board[0][0] == c and board[1][1] == c and board[2][2] == c or \
               board[0][2] == c and board[1][1] == c and board[2][0] == c


if __name__ == '__main__':
    board = ["O  ", "   ", "   "]
    print(Solution().validTicTacToe(board))
