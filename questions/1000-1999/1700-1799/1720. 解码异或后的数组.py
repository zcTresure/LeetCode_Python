# File Name:  1720. 解码异或后的数组
# date:       2021/5/11
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for num in encoded:
            arr.append(arr[-1] ^ num)
        return arr


test = Solution()
encoded = [1, 2, 3]
first = 1
print(test.decode(encoded, first))
