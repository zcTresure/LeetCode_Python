# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "zcTresure"

from collections import defaultdict


class Solution:
    def sortByBits(self, arr: list) -> list:
        bins = defaultdict(list)
        for num in arr:
            count, tmp = 0, num
            while tmp:
                count += tmp % 2
                tmp //= 2
            bins[count].append(num)
        res = list()
        for i in range(15):
            if bins[i]:
                res += sorted(bins[i])
        return res

    def sortByBits(self, arr: list) -> list:
        bins = [0] * 10001
        for i in range(1, 10001):
            bins[i] = bins[i >> 1] + i % 2
        dic = defaultdict(list)
        for num in arr:
            dic[bins[num]].append(num)
        res = list()
        for i in range(15):
            if dic[i]:
                res += sorted(dic[i])
        return res

    def sortByBits(self, arr: list) -> list:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
test = Solution()
print(test.sortByBits(arr))
