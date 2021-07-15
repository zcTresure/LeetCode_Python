# -*- coding: utf-8 -*-
# File:      1846. 减小和重新排列数组后的最大元素.py
# DATA:      2021/7/15
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    # 贪心
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            arr[i] = min(arr[i], arr[i - 1] + 1)  # 每次用当前元素 和 前元素+1 比较, 选择最小的
        return arr[-1]

    # 计数排序
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        cnt = [0] * (n + 1)
        for num in arr:
            cnt[min(num, n)] += 1  # 记录数字出现的次数, 大于列表长度n的只选n
        miss = 0
        for i in range(1, n + 1):
            if cnt[i] == 0:
                miss += 1
            else:
                miss -= min(miss, cnt[i] - 1)  # miss不会小于0, 所以最多减去 miss
        return n - miss


arr = [2, 1, 1, 2, 2, 1]
arr = [100, 1, 1000]
print(Solution().maximumElementAfterDecrementingAndRearranging(arr))
