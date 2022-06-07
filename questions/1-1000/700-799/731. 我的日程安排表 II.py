# -*- coding: utf-8 -*-
# File:      731. 我的日程安排表 II.py
# DATA:      2022/6/6
# Software:  PyCharm
__author__ = 'zcFang'


class MyCalendarTwo:

    def __init__(self):
        self.calendar = []  # 所有能够存在的时间段
        self.overlaps = []  # 重复过一次的时间段

    def book(self, start: int, end: int) -> bool:
        for i, j in self.overlaps:
            if start < j and end > i:  # 判断时间段是否已经重复过一次
                return False
        for i, j in self.calendar:
            if start < j and end > i:  # 时间段是否已经存在
                self.overlaps.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
