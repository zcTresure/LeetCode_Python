# -*- coding: utf-8 -*-
# File:      729. 我的日程安排表 I.py
# DATA:      2022/6/6
# Software:  PyCharm
__author__ = 'zcFang'


class MyCalendar:
    # 暴力
    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.calendar:
            if s < end and start < e:
                return False
        self.calendar.append((start, end))
        return True

class MyCalendar:
    # 平衡树
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.root.inseart(Node(start, end))


class Node:
    __slots__ = 'start', 'end', 'left', 'right'

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None

    def inseart(self, node):
        if node.start >= self.end:
            if not self.right :
                self.right = node
                return True
            return self.right.inseart(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.inseart(node)
        else:
            return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
