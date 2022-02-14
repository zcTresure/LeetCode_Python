# -*- coding: utf-8 -*-
# File:    1342. 将数字变成 0 的操作次数.py
# Date:    2022/2/14
# Software: Pycharm
__author__ = 'zcFang'


class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans = 0
        while num:
            ans += num & 1
            if num > 1:
                ans += 1
            num >>= 1
        return ans

    # 模拟
    def numberOfSteps(self, num: int) -> int:
        ans = 0
        while num != 0:
            ans += 1
            num = num - 1 if num & 1 else num // 2
        return ans


print(Solution().numberOfSteps(num=123))
