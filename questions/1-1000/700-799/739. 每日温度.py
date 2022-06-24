# -*- coding: utf-8 -*-
# File:      739. 每日温度.py
# DATA:      2022/6/24
# Software:  PyCharm
from typing import List


class Solution:
    # 暴力
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans, nxt, big = [0] * n, dict(), 10 ** 9
        for i in range(n - 1, -1, -1):
            warmer_index = min(nxt.get(t, big) for t in range(temperatures[i] + 1, 102))
            if warmer_index != big:
                ans[i] = warmer_index - i
            nxt[temperatures[i]] = i
        return ans

    # 单调栈
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        ans = [0] * length
        stack = []
        for i in range(length):
            temperature = temperatures[i]
            while stack and temperature > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans


print(Solution().dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
