# Date:       2021/2/1
# encode:      UTF-8
__author__ = "zcTresure"

from typing import List


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sumA, sumB = sum(A), sum(B)
        delta = (sumA - sumB) // 2
        rec = set(A)
        ans = []
        for y in B:
            x = y + delta
            if x in rec:
                return [x, y]


test = Solution()
A = [1, 1]
B = [2, 2]
print(test.fairCandySwap(A, B))
