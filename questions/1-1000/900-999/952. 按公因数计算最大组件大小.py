# -*- coding: utf-8 -*-
# File:    952. 按公因数计算最大组件大小.py
# Date:    2022/8/1
# Software: Pycharm
from collections import Counter
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x: int, y: int) -> None:
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            self.rank[x] += 1


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        uf = UnionFind(max(nums) + 1)
        for num in nums:
            i = 2
            while i * i <= num:
                if num % i == 0:
                    uf.merge(num, i)
                    uf.merge(num, num // i)
                i += 1
        return max(Counter(uf.find(num) for num in nums).values())


print(Solution().largestComponentSize(nums=[4, 6, 15, 35]))
