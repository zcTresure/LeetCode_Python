# -*- coding: utf-8 -*-
# File:      715. Range 模块.py
# DATA:      2022/6/20
# Software:  PyCharm
from sortedcontainers import SortedDict


class RangeModule:

    def __init__(self):
        self.intervals = SortedDict()

    def addRange(self, left: int, right: int) -> None:
        itvs = self.intervals

        x = itvs.bisect_right(left)
        if x != 0:
            start = x - 1
            if itvs.values()[start] >= right:
                return
            if itvs.values()[start] >= left:
                left = itvs.keys()[start]
                itvs.popitem(start)
                x -= 1

        while x < len(itvs) and itvs.keys()[x] <= right:
            right = max(right, itvs.values()[x])
            itvs.popitem(x)

        itvs[left] = right

    def queryRange(self, left: int, right: int) -> bool:
        itvs = self.intervals

        x = itvs.bisect_right(left)
        if x == 0:
            return False

        return right <= itvs.values()[x - 1]

    def removeRange(self, left: int, right: int) -> None:
        itvs = self.intervals

        x = itvs.bisect_right(left)
        if x != 0:
            start = x - 1
            if (ri := itvs.values()[start]) >= right:
                if (li := itvs.keys()[start]) == left:
                    itvs.popitem(start)
                else:
                    itvs[li] = left
                if right != ri:
                    itvs[right] = ri
                return
            elif ri > left:
                itvs[itvs.keys()[start]] = left

        while x < len(itvs) and itvs.keys()[x] < right:
            if itvs.values()[x] <= right:
                itvs.popitem(x)
            else:
                itvs[right] = itvs.values()[x]
                itvs.popitem(x)
                break

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
