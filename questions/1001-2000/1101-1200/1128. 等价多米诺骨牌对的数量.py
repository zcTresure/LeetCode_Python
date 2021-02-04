# Date:       2021/1/29
# Coding:      UTF-8
__author__ = "zcTresure"

from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        num = [0] * 100
        ret = 0
        for x, y in dominoes:
            val = (x * 10 + y if x <= y else y * 10 + x)
            ret += num[val]
            num[val] += 1
        return ret


test = Solution()
dominoes = [[1, 2], [2, 1], [3, 4], [5, 6]]
print(test.numEquivDominoPairs(dominoes))
