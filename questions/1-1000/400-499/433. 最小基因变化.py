# -*- coding: utf-8 -*-
# File:      433. 最小基因变化.py
# DATA:      2022/5/7
# Software:  PyCharm
__author__ = 'zcFang'

from collections import deque
from typing import List


class Solution:
    # 广度优先搜索
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 1
        bank = set(bank)
        if end not in bank:
            return -1
        q = deque([(start, 0)])
        while q:
            cur, step = q.popleft()
            for i, x in enumerate(cur):
                for y in "ACGT":
                    if x != y:
                        nxt = cur[:i] + y + cur[i + 1:]
                        if nxt in bank:
                            if nxt == end:
                                return step + 1
                            bank.remove(nxt)
                            q.append((nxt, step + 1))
        return -1

    # 预处理优化
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0

        def diffOne(s: str, t: str) -> bool:
            return sum(x != y for x, y in zip(s, t)) == 1

        m = len(bank)
        adj = [[] for _ in range(m)]
        end_index = -1
        for i, s in enumerate(bank):
            if s == end:
                end_index = i
            for j in range(i + 1, m):
                if diffOne(s, bank[j]):
                    adj[i].append(j)
                    adj[j].append(i)
        if end_index == -1:
            return -1
        q = [i for i, s in enumerate(bank) if diffOne(start, s)]
        visited = set(q)
        step = 1
        while q:
            tmp = q
            q = []
            for cur in tmp:
                if cur == end_index:
                    return step
                for nxt in adj[cur]:
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)
            step += 1
        return -1


start = "AACCGGTT"
end = "AACCGGTA"
bank = ["AACCGGTA"]
print(Solution().minMutation(start, end, bank))
