# -*- coding: utf-8 -*-
# File:    238. 除自身以外数组的乘积.py
# Date:    2021/12/26
# Software: Pycharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l_prod, r_prod = [0] * n, [0] * n
        ans = [0] * n
        l_prod[0] = 1
        for i in range(1, n):
            l_prod[i] = l_prod[i - 1] * nums[i - 1]
        r_prod[n - 1] = 1
        for i in range(n - 2, -1, -1):
            r_prod[i] = r_prod[i + 1] * nums[i + 1]
        for i in range(n):
            ans[i] = l_prod[i] * r_prod[i]
        return ans

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        ans[0] = 1
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]
        r_prod = 1
        for i in reversed(range(n)):
            ans[i] *= r_prod
            r_prod *= nums[i]
        return ans


nums = [1, 2, 3, 4]
print(Solution().productExceptSelf(nums))
