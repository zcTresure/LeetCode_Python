# -*- coding: utf-8 -*-
# File:     483. 最小好进制.py
# Date:     2021/6/18
# Software: PyCharm
__author__ = 'zcFang'


class Solution:
    def smallestGoodBase(self, n: str) -> str:
        def check(x, m):  # 计算倍数+1
            ans = 0
            for _ in range(m + 1):
                ans = ans * x + 1
            return ans

        num = int(n)
        ans = float('inf')
        for i in range(1, 64):
            left, right = 2, num
            while left < right:
                mid = left + (right - left) // 2
                tmp = check(mid, i)
                if tmp == num:
                    ans = min(ans, mid)
                    break
                elif tmp < num:
                    left = mid + 1
                else:
                    right = mid
        return str(ans)

print(Solution().smallestGoodBase('10000000000000'))
