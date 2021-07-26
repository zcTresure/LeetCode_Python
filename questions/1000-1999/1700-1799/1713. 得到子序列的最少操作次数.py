# -*- coding: utf-8 -*-
# File:    1713. 得到子序列的最少操作次数.py
# Date:    2021/7/26
# Software: Pycharm
__author__ = 'zcFang'

import bisect
from typing import List


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:  # target中的数字各不相同
        idx_dict = {num: i for i, num in enumerate(target)}  # 集合存储 目标数组数字对应下标
        stack = []
        for num in arr:
            if num in idx_dict:  # 数字在目标数组中存在
                idx = idx_dict[num]  # 记录目标数组中的下标
                i = bisect.bisect_left(stack, idx)  # 查找目标数组中数字的下标是否在stack中的下标
                if i == len(stack):  # 不在则插入
                    stack.append(idx)
                stack[i] = idx  # 在或不在都可更新下标
        return len(target) - len(stack)


target = [5, 1, 3]
arr = [9, 4, 2, 3, 4]
print(Solution().minOperations(target, arr))
