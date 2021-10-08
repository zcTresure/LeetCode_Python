# -*- coding: utf-8 -*-
# File:      284. 顶端迭代器.py
# DATA:      2021/10/8
# Software:  PyCharm
__author__ = 'zcFang'


class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self._next = iterator.next()
        self._hasNext = iterator.hasNext()

    def peek(self):
        return self._next

    def next(self):
        ret = self._next
        self._hasNext = self.iterator.hasNext()
        self._next = self.iterator.next() if self._hasNext else 0
        return ret

    def hasNext(self):
        return self._hasNext
