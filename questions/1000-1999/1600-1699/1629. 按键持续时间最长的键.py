# -*- coding: utf-8 -*-
# File:    1629. 按键持续时间最长的键.py
# Date:    2022/1/9
# Software: Pycharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        ans = keysPressed[0]
        max_time = releaseTimes[0]
        for i in range(1, len(keysPressed)):
            key = keysPressed[i]
            time = releaseTimes[i] - releaseTimes[i - 1]
            if time > max_time or time == max_time and key > ans:
                ans = key
                max_time = time
        return ans


releaseTimes = [9, 29, 49, 50]
keysPressed = "cbcd"
print(Solution().slowestKey(releaseTimes, keysPressed))
