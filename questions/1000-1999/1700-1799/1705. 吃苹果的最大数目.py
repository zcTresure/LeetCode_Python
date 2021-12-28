# -*- coding: utf-8 -*-
# File:      1705. 吃苹果的最大数目.py
# DATA:      2021/12/24
# Software:  PyCharm
__author__ = 'zcFang'

import heapq
from typing import List


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        pq = []
        ans, i, n = 0, 0, len(apples)

        while i < n:  # 第一阶段，苹果树上还在生产苹果
            while pq and pq[0][0] <= i:
                heapq.heappop(pq)  # 队列中苹果已经腐烂，出队列
            if apples[i] > 0:  # 当天苹果产量不为零
                heapq.heappush(pq, [i + days[i], apples[i]])  # 当天苹果产量和腐烂时间
            if pq:
                pq[0][1] -= 1  # 腐烂时间缩短
                if (pq[0][1] == 0):
                    heapq.heappop(pq)
                ans += 1  # 吃的苹果数量加一
            i += 1  # 天数自增

        while pq:  # 第二阶段，苹果树不再生产苹果
            while pq and pq[0][0] <= i:
                heapq.heappop(pq)  # 队列中苹果已经腐烂，出队列
            if len(pq) == 0:
                return ans
            num = min(pq[0][0] - i, pq[0][1])  # 取苹果数量和腐烂天数的较小的那一个
            ans += num
            i += num
            heapq.heappop(pq)
        return ans


apples = [1, 2, 3, 5, 2]
days = [3, 2, 1, 4, 2]
print(Solution().eatenApples(apples, days))
