# -*- coding: utf-8 -*-
# File:      869. 重新排序得到 2 的幂.py
# DATA:      2021/10/28
# Software:  PyCharm
__author__ = 'zcFang'

from typing import Tuple


class Solution:
    # 回溯 + 位运算
    def isPowerofTwo(self, n: int) -> bool:
        return (n & (n - 1)) == 0

        nums = sorted(list(str(n)))
        m = len(nums)
        visited = [False] * m

        def backtrack(index: int, num: int) -> bool:
            if index == m:
                return self.isPowerofTwo(num)
            for i, ch in enumerate(nums):
                if (num == 0 and ch == '0') or visited[i] or (i > 0 and not visited[i - 1] and ch == nums[i - 1]):
                    continue
                visited[i] = True
                if backtrack(index + 1, num * 10 + ord(ch) - ord('0')):
                    return True
                visited[i] = False
            return False

        return backtrack(0, 0)

    # 预处理 + 哈希表
    def reorderedPowerOf2(self, n: int) -> bool:
        def countDigits(n: int) -> Tuple[int]:
            cnt = [0] * 10
            while n:
                cnt[n % 10] += 1
                n //= 10
            return tuple(cnt)

        powerOfTwoDigits = {countDigits(1 << i) for i in range(30)}
        return countDigits(n) in powerOfTwoDigits


print(Solution().reorderedPowerOf2(265))
