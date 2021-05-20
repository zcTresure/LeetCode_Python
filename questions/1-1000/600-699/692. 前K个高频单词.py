# -*- coding: utf-8 -*-
# File:     692. 前K个高频单词.py
# Date:     2021/5/20
# Software: PyCharm
__author__ = 'zcFang'

import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return list(map(lambda x: x[0], heapq.nsmallest(k, Counter(words).items(), key=lambda x: (-x[1], x[0]))))


words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
test = Solution()
print(test.topKFrequent(words, k))
