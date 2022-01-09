# -*- coding: utf-8 -*-
# File:    89. 格雷编码.py
# Date:    2022/1/8
# Software: Pycharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1, n + 1):
            for j in range(len(ans) - 1, -1, -1):
                ans.append(ans[j] | (1 << (i - 1)))
        return ans


print(Solution().grayCode(2))