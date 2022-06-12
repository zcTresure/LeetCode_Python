# -*- coding: utf-8 -*-
# File:      1436. 旅行终点站.py
# DATA:      2021/10/8
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        citiesA = {path[0] for path in paths}
        return next(path[1] for path in paths if path[1] not in citiesA)


paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
print(Solution().destCity(paths))
