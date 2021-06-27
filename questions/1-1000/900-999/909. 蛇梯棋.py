# -*- coding: utf-8 -*-
# File:     909. 蛇梯棋.py
# Date:     2021/6/27
# Software: PyCharm
__author__ = 'zcFang'

from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def id2rc(index: int) -> (int, int):
            nonlocal n
            row, col = (index - 1) // n, (index - 1) % n
            if row % 2 == 1:  # 奇数行，列移动方向向左
                col = n - 1 - col
            return n - 1 - row, col

        visited = set()  # 访问过的集合
        q = deque([(1, 0)])
        while q:
            index, step = q.popleft()
            for i in range(1, 6 + 1):  # 遍历六种情况
                index_next = index + i
                if index_next > n * n:  # 超出边界
                    break
                x_next, y_next = id2rc(index_next)  # 得到下一步的行列
                if board[x_next][y_next] > 0:  # 存在蛇和梯子
                    index_next = board[x_next][y_next]
                if index_next == n * n:  # 到达终点
                    return step + 1
                if index_next not in visited:  # 位置不在访问集合内
                    visited.add(index_next)
                    q.append((index_next, step + 1))  # 扩展新状态
        return -1


board = [[-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 35, -1, -1, 13, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 15, -1, -1, -1, -1]]
print(Solution().snakesAndLadders(board))
