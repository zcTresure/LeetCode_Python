# -*- coding: utf-8 -*-
# File:      2049. 统计最高分的节点数目.py
# DATA:      2022/3/11
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        children = [[] for _ in range(n)]
        for node, parent in enumerate(parents):
            if parent != -1:
                children[parent].append(node)

        max_score, cnt = 0, 0

        def dfs(node: int) -> int:
            score = 1
            size = n - 1
            for ch in children[node]:
                sz = dfs(ch)
                score *= sz
                size -= sz
            if node != 0:
                score *= size
            nonlocal max_score, cnt
            if score == max_score:
                cnt += 1
            elif score > max_score:
                max_score, cnt = score, 1
            return n - size

        dfs(0)
        return cnt


parents = [-1, 2, 0, 2, 0]
print(Solution().countHighestScoreNodes(parents))
