# -*- coding: utf-8 -*-
# File:      786. 第 K 个最小的素数分数.py
# DATA:      2021/11/29
# Software:  PyCharm
__author__ = 'zcFang'

import heapq
from functools import cmp_to_key
from typing import List, Tuple


class Frac:
    def __init__(self, idx: int, idy: int, x: int, y: int) -> None:
        self.idx = idx
        self.idy = idy
        self.x = x
        self.y = y

    def __lt__(self, other: "Frac") -> bool:
        return self.x * other.y < self.y * other.x


class Solution:
    # 自定义排序
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        def cmp(x: Tuple[int, int], y: Tuple[int, int]) -> int:
            return -1 if x[0] * y[1] < x[1] * y[0] else 1

        n = len(arr)
        frac = list()
        for i in range(n):
            for j in range(i + 1, n):
                frac.append((arr[i], arr[j]))

        frac.sort(key=cmp_to_key(cmp))
        return list(frac[k - 1])

    # 优先队列
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        q = [Frac(0, i, arr[0], arr[i]) for i in range(1, n)]
        heapq.heapify(q)
        for _ in range(k - 1):
            frac = heapq.heappop(q)
            i, j = frac.idx, frac.idy
            if i + 1 < j:
                heapq.heappush(q, Frac(i + 1, j, arr[i + 1], arr[j]))
        return [q[0].x, q[0].y]

    # 二分查找+双指针
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        left, right = 0.0, 1.0

        while True:
            mid = (left + right) / 2
            i, count = -1, 0
            # 记录最大的分数
            x, y = 0, 1

            for j in range(1, n):
                while arr[i + 1] / arr[j] < mid:
                    i += 1
                    if arr[i] * y > arr[j] * x:
                        x, y = arr[i], arr[j]
                count += i + 1

            if count == k:
                return [x, y]

            if count < k:
                left = mid
            else:
                right = mid


arr = [1, 2, 3, 5]
k = 3
print(Solution().kthSmallestPrimeFraction(arr, k))
