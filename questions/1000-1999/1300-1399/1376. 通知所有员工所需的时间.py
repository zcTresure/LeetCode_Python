# -*- coding: utf-8 -*-
# File:      1376. 通知所有员工所需的时间.py
# DATA:      2022/6/29
# Software:  PyCharm
from collections import defaultdict, deque
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        visited = [False] * n
        result = 0
        for i in range(n):
            if visited[i]:
                continue
            total = 0
            while manager[i] != -1:
                visited[i] = True
                i = manager[i]
                total += informTime[i]
            result = max(total, result)
        return result

    total = 0

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tmp = defaultdict(list)

        for i in range(len(manager)):
            tmp[manager[i]].append(i)

        self.dfs(tmp, informTime, headID, 0)
        return self.total

    def dfs(self, tmp, informTime, head_id, total):
        if not tmp[head_id]:
            self.total = max(self.total, total)
        for id_ in tmp[head_id]:
            self.dfs(tmp, informTime, id_, total + informTime[head_id])
        def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
            q = deque()
            tmp = defaultdict(list)
            for i in range(len(manager)):
                if manager[i] == -1:
                    continue
                tmp[manager[i]].append(i)
            q.append((headID, 0))
            result = 0
            while q:
                this_id, val = q.popleft()

                for id_ in tmp[this_id]:
                    q.append((id_, val + informTime[this_id]))
                    result = max(result, val + informTime[this_id])
            return result
