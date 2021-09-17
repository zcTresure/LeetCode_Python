# -*- coding: utf-8 -*-
# File:      36. 有效的数独.py
# DATA:      2021/9/17
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0] * 9 for _ in range(9)]
        cols = [[0] * 9 for _ in range(9)]
        sub_boxes = [[[0] * 9 for _ in range(3)] for _ in range(3)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    index = ord(board[i][j]) - ord('0') - 1
                    rows[i][index] += 1
                    cols[index][j] += 1
                    sub_boxes[i // 3][j // 3][index] += 1
                    if rows[i][index] > 1 or cols[index][j] > 1 or sub_boxes[i // 3][j // 3][index] > 1:
                        return False
        return True


board = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(Solution().isValidSudoku(board))
