# -*- coding: utf-8 -*-
# File:    373. 查找和最小的 K 对数字.py
# Date:    2022/1/14
# Software: Pycharm
__author__ = 'zcFang'

import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        m, n = len(nums1), len(nums2)
        pq = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, m))]
        while pq and len(ans) < k:
            _, i, j = heapq.heappop(pq)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heapq.heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))

        return ans


print(Solution().kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3))
print(Solution().kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2))
print(Solution().kSmallestPairs(nums1=[1, 2], nums2=[3], k=3))
