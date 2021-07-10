# -*- coding: utf-8 -*-
# File:      981. 基于时间的键值存储.py
# DATA:      2021/7/10
# Software:  PyCharm
__author__ = 'zcFang'

from bisect import bisect_right
from collections import defaultdict


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        return "" if (a := bisect_right(self.dic[key], [timestamp, 'z' * 101])) == 0 else self.dic[key][a - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
titles = ["TimeMap", "set", "get", "get", "set", "get", "get"]
inputs = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
