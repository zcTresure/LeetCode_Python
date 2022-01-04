# -*- coding: utf-8 -*-
# File:      155. 最小栈.py
# DATA:      2022/1/4
# Software:  PyCharm
__author__ = 'zcFang'

import math


class MinStack:

    def __init__(self):
        self.min_stack = [math.inf]
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
