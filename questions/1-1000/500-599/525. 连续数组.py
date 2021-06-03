# -*- coding: utf-8 -*-
# File:     525. 连续数组.py
# Date:     2021/6/3
# Software: PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = {0: -1}# 前缀和字典: key为1的数量和0的数量的差值,value为对应坐标
        counter = ans = 0# 当前1的数量和0的数量的差值
        for i, num in enumerate(nums):
            if num:# 每多一个1，差值+1
                counter += 1
            else:# 每多一个0，差值-1
                counter -= 1
            # 如果存在1和0的数量差值相等的地方，那么说明后者到前者之前1和0的数量相等！
            if counter in hashmap:
                ans = max(ans, i - hashmap[counter])
            else:
                hashmap[counter] = i
        return ans


nums = [0, 1, 0]
print(Solution().findMaxLength(nums))
