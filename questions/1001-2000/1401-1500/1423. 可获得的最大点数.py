# Date:       2021/2/8
# Coding:      UTF-8
__author__ = "zcTresure"

from typing import List
from itertools import accumulate


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        windowSize = n - k
        s = sum(cardPoints[:windowSize])
        minPoint = s
        for i in range(windowSize, n):
            s += cardPoints[i] - cardPoints[i - windowSize]
            minPoint = min(minPoint, s)

        return sum(cardPoints) - minPoint


cardPoints = [1, 2, 3, 4, 5, 6, 1]
k = 3
test = Solution()
print(test.maxScore(cardPoints, k))
