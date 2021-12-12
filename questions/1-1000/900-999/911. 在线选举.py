# -*- coding: utf-8 -*-
# File:      911. 在线选举.py
# DATA:      2021/12/11
# Software:  PyCharm
__author__ = 'zcFang'

from collections import defaultdict
from typing import List


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        tops = []
        vote_counts = defaultdict()
        vote_counts[-1] = -1
        top = -1
        for p in persons:
            vote_counts[p] = vote_counts.get(p, 0) + 1
            if vote_counts[p] >= vote_counts[top]:
                top = p
            tops.append(top)
        self.tops = tops
        self.times = times

    def q(self, t: int) -> int:
        left, right = 0, len(self.times) - 1
        # 找到满足 times[l] <= t 的最大的 l
        while left < right:
            mid = left + (right + 1) // 2
            if self.times[mid] <= t:
                left = mid
            else:
                right = mid - 1
        return self.tops[left]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
