# File Name:  1734. 解码异或后的排列
# date:       2021/5/11
# encode:      UTF-8
__author__ = 'zcTresure'

from functools import reduce
from operator import xor
from typing import List


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        total = reduce(xor, range(1, n + 1))  # 异或1~n之间的所有数
        odd = 0
        for i in range(1, n - 1, 2):  # 每隔两位异或encoded中的数等于异或加密数组prem中除了第一位之外的所有数
            odd ^= encoded[i]
        prem = [total ^ odd]  # 得prem数组中的第一位数
        for i in range(n - 1):
            prem.append(prem[-1] ^ encoded[i])  # 逐位与前一位异或，还原加密数组prem
        return prem


test = Solution()
encoded = [6, 5, 4, 6]
print(test.decode(encoded))
