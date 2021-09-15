# -*- coding: utf-8 -*-
# File:      1093. 大样本统计.py
# DATA:      2021/9/15
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        n = len(count)
        mode = mode_max = 0
        min_num = max_num = -1
        avg = mid_num = 0
        size = 0
        for i in range(n):
            if count[i] != 0:
                size += count[i]
                avg += 1.0 * count[i] * i
                if count[i] > mode_max:
                    mode_max = count[i]
                    mode = i
                if min_num == -1:
                    min_num = i
                max_num = i
        # 求中位数
        sum_count = 0
        for i in range(n):
            sum_count += count[i]
            if sum_count << 1 > size:  # 奇数个
                mid_num = i
                break
            elif sum_count << 1 == size:  # 偶数个
                for j in range(i + 1, n):
                    if count[j] != 0:
                        mid_num = (i + j) / 2.0
                        break
                break
        return [min_num, max_num, avg / size, mid_num, mode]


count = [0, 1, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(Solution().sampleStats(count))
