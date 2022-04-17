# -*- coding: utf-8 -*-
# File:      380. O(1) 时间插入、删除和获取随机元素.py
# DATA:      2022/4/13
# Software:  PyCharm
__author__ = 'zcFang'

from random import choice


class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.indices[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        idx = self.indices[val]
        self.nums[idx] = self.nums[-1]
        self.indices[self.nums[idx]] = idx
        self.nums.pop()
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        return choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
