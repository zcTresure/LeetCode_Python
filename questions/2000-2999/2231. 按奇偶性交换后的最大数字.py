# -*- coding: utf-8 -*-
# File:      2231. 按奇偶性交换后的最大数字.py
# DATA:      2022/5/29
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def largestInteger(self, num: int) -> int:
        # 转化为各位数值的数组
        l = [int(c) for c in str(num)]
        n = len(l)
        # 选择排序
        for i in range(n - 1):
            for j in range(i + 1, n):
                # 数值奇偶相同的才判断
                if (l[i] - l[j]) % 2 == 0 and l[i] < l[j]:
                    l[i], l[j] = l[j], l[i]
        return int("".join(str(c) for c in l))


print(Solution().largestInteger(1234))
