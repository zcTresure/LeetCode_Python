# -*- coding: utf-8 -*-
# File:     1442. 形成两个异或相等数组的三元组数目.py
# Date:     2021/5/18
# Software: PyCharm
__author__ = 'zcFang'

from collections import Counter
from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        prefix = [0]
        for val in arr:
            prefix.append(prefix[-1] ^ val)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j, n):
                    if prefix[i] == prefix[k + 1]:
                        ans += 1
        return ans

    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        prefix = [0]
        for val in arr:
            prefix.append(prefix[-1] ^ val)
        for i in range(n):
            for k in range(i + 1, n):
                if prefix[i] == prefix[k + 1]:
                    ans += k - i
        return ans

    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        prefix = [0]
        for val in arr:
            prefix.append(prefix[-1] ^ val)
        cnt, total = Counter(), Counter()
        for k in range(n):
            if prefix[k + 1] in cnt:
                ans += cnt[prefix[k + 1]] * k - total[prefix[k + 1]]
            cnt[prefix[k]] += 1
            total[prefix[k]] += k
        return ans

    def countTriplets(self, arr: List[int]) -> int:
        cnt, total = Counter(), Counter()
        ans = s = 0
        for k, val in enumerate(arr):
            if (t := s ^ val) in cnt:
                ans += cnt[t] * k - total[t]
            cnt[s] += 1
            total[s] += k
            s = t
        return ans

    def countTriplets(self, arr: List[int]) -> int:
        cnt, total = Counter(), Counter()
        ans = x = 0
        for k, val in enumerate(arr):
            # 计数的语句可以放在前面
            cnt[x] += 1
            total[x] += k
            x ^= val
            if x in cnt:
                ans += cnt[x] * k - total[x]
        return ans


arr = [2, 3, 1, 6, 7, 1]
test = Solution()
print(test.countTriplets(arr))
