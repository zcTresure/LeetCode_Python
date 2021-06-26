# -*- coding: utf-8 -*-
# File:     773. 滑动谜题.py
# Date:     2021/6/26
# Software: PyCharm
__author__ = 'zcFang'

import heapq
from collections import deque
from typing import List, Generator


class AStar:
    DIST = [
        [0, 1, 2, 1, 2, 3],
        [1, 0, 1, 2, 1, 2],
        [2, 1, 0, 3, 2, 1],
        [1, 2, 3, 0, 1, 2],
        [2, 1, 2, 1, 0, 1],
        [3, 2, 1, 2, 1, 0],
    ]

    # 计算启发函数
    @staticmethod
    def getH(status: str) -> int:
        ret = 0
        for i in range(6):
            if status[i] != "0":
                ret += AStar.DIST[i][int(status[i]) - 1]
        return ret

    def __init__(self, status: str, g: str) -> None:
        self.status = status
        self.g = g
        self.h = AStar.getH(status)
        self.f = self.g + self.h

    def __lt__(self, other: "AStar") -> bool:
        return self.f < other.f


class Solution:
    NEIGHBORS = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
    TARGET = '123450'

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # 枚举 status 通过一次交换操作得到的状态
        def get(status: str) -> Generator[str, None, None]:
            s = list(status)
            x = s.index('0')
            for y in Solution.NEIGHBORS[x]:
                s[x], s[y] = s[y], s[x]
                yield ''.join(s)
                s[x], s[y] = s[y], s[x]

        initial = ''.join(str(num) for num in sum(board, []))
        if initial == Solution.TARGET:
            return 0
        q = deque([(initial, 0)])
        seen = {initial}
        while q:
            status, step = q.popleft()
            for next_status in get(status):
                if next_status not in seen:
                    if next_status == Solution.TARGET:
                        return step + 1
                    q.append((next_status, step + 1))
                    seen.add(next_status)
        return -1


    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # 枚举 status 通过一次交换操作得到的状态
        def get(status: str) -> Generator[str, None, None]:
            s = list(status)
            x = s.index("0")
            for y in Solution.NEIGHBORS[x]:
                s[x], s[y] = s[y], s[x]
                yield "".join(s)
                s[x], s[y] = s[y], s[x]

        initial = "".join(str(num) for num in sum(board, []))
        if initial == Solution.TARGET:
            return 0

        q = [AStar(initial, 0)]
        seen = {initial}
        while q:
            node = heapq.heappop(q)
            for next_status in get(node.status):
                if next_status not in seen:
                    if next_status == Solution.TARGET:
                        return node.g + 1
                    heapq.heappush(q, AStar(next_status, node.g + 1))
                    seen.add(next_status)

        return -1


board = [[1, 2, 3], [5, 4, 0]]
print(Solution().slidingPuzzle(board))
