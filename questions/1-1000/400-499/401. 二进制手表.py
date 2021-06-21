# -*- coding: utf-8 -*-
# File:     401. 二进制手表.py
# Date:     2021/6/21
# Software: PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for h in range(12):
            for m in range(60):
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    ans.append(f"{h}:{m:02d}")
        return ans

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = list()
        for i in range(1024):
            h, m = i >> 6, i & 0x3f  # 用位运算取出高 4 位和低 6 位
            if h < 12 and m < 60 and bin(i).count("1") == turnedOn:
                ans.append(f"{h}:{m:02d}")
        return ans


turnedOn = int(input("输入整数："))
print(Solution().readBinaryWatch(turnedOn))
