# File Name:  1104. 二叉树寻路
# date:       2021/4/14
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List
from collections import deque


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        result = deque()
        while label != 1:
            result.appendleft(label)
            label >>= 1
            label ^= ((1 << (label.bit_length() - 1)) - 1)
        return [1] + list(result)


label = int(input("输入数字:"))
test = Solution()
print(test.pathInZigZagTree(label))
