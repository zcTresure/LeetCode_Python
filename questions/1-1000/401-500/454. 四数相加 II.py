

__author__ = "zcTresure"

from collections import Counter


class Solution:
    def fourSumCount(self, A: list, B: list, C: list, D: list) -> int:
        countAB = Counter(u + v for u in A for v in B)
        ans = 0
        for u in C:
            for v in D:
                if -u - v in countAB:
                    ans += countAB[-u - v]
        return ans


A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
test = Solution()
print(test.fourSumCount(A, B, C, D))
