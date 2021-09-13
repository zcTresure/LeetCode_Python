# -*- coding: utf-8 -*-
# File:      955. 删列造序 II.py
# DATA:      2021/9/11
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    # 贪心
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        cur = [""] * len(strs)
        for col in zip(*strs):  # 取每行同列字符
            cur2 = cur[:]
            for i, letter in enumerate(col):
                cur2[i] = cur2[i] + letter
            # 当前列为字典序，更新列表
            if all(cur2[i] <= cur2[i + 1] for i in range(len(cur2) - 1)):
                cur = cur2
            else:
                ans += 1  # 当前列为无序，删除该列
        return ans

    # 贪心 + 空间
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        cuts = [False] * (len(strs) - 1)
        for col in zip(*strs):  # 取每行同列字符
            # 当前列为字典序，更新列表
            if all(cuts[i] or col[i] <= col[i + 1] for i in range(len(col) - 1)):
                for i in range(len(col) - 1):
                    if col[i] < col[i + 1]:
                        cuts[i] = True
            else:  # 当前列为无序，删除该列
                ans += 1
        return ans


strs = ["zyx", "wvu", "tsr"]
print(Solution().minDeletionSize(strs))
