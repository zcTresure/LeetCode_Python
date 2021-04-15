# Date:       2020/12/25
# encode:      UTF-8
__author__ = "zcTresure"

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        arrCandys = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                arrCandys[i] = arrCandys[i - 1] + 1
        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                arrCandys[i - 1] = max(arrCandys[i - 1], arrCandys[i] + 1)
        return sum(arrCandys)


ratings = [1, 0, 2]
test = Solution()
print(test.candy(ratings))
