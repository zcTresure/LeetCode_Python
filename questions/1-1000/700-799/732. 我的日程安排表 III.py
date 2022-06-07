# -*- coding: utf-8 -*-
# File:      732. 我的日程安排表 III.py
# DATA:      2022/6/6
# Software:  PyCharm
__author__ = 'zcFang'

from collections import defaultdict

from sortedcontainers import SortedDict


class MyCalendarThree:
    # 差分数组
    def __init__(self):
        self.d = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.d[start] = self.d.setdefault(start, 0) + 1
        self.d[end] = self.d.setdefault(end, 0) - 1
        ans = max_book = 0
        for freq in self.d.values():
            max_book += freq
            ans = max(ans, max_book)
        return ans


class MyCalendarThree:
    # 线段树
    def __init__(self):
        self.tree = defaultdict(int)
        self.lazy = defaultdict(int)

    def update(self, start: int, end: int, l: int, r: int, index: int):
        if r < start or l > end:
            return
        if start <= l and r <= end:
            self.tree[index] += 1
            self.lazy[index] += 1
        else:
            mid = (l + r) // 2
            self.update(start, end, l, mid, index * 2)
            self.update(start, end, mid + 1, r, index * 2 + 1)
            self.tree[index] = self.lazy[index] + max(self.tree[index * 2], self.tree[index * 2 + 1])

    def book(self, start: int, end: int) -> int:
        self.update(start, end - 1, 0, 10 ** 9, 1)
        return self.tree[1]

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
