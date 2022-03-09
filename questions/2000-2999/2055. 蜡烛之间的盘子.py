# -*- coding: utf-8 -*-
# File:      2055. 蜡烛之间的盘子.py
# DATA:      2022/3/8
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    # 预处理 + 前缀和
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        pre_sum, sum = [0] * n, 0
        left, l = [0] * n, -1
        # 计算前缀和 + 左边 蜡烛位置
        for i, ch in enumerate(s):
            if ch == '*':
                sum += 1
            else:
                l = i
            pre_sum[i] = sum
            left[i] = l

        # 计算右边蜡烛位置
        right, r = [0] * n, -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                r = i
            right[i] = r

        ans = [0] * len(queries)
        for i, (x, y) in enumerate(queries):
            x, y = right[x], left[y]
            if x >= 0 and y >= 0 and x < y:
                ans[i] = pre_sum[y] - pre_sum[x]
        return ans


s = "***|**|*****|**||**|*"
queries = [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]
print(Solution().platesBetweenCandles(s, queries))
