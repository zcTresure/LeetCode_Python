# -*- coding: utf-8 -*-
# File:      630. 课程表 III.py
# DATA:      2021/12/14
# Software:  PyCharm
__author__ = 'zcFang'

import heapq
from collections import deque
from typing import List


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda c: c[1])
        q = []
        total = 0  # 优先队列中所有课程的总时间

        for ti, di in courses:
            if total + ti <= di:
                total += ti
                heapq.heappush(q, -ti)  # 最小堆
            elif q and -q[0] > ti:
                total -= -q[0] - ti
                heapq.heappop(q)
                heapq.heappush(q, -ti)

        return len(q)


courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
print(Solution().scheduleCourse(courses))
