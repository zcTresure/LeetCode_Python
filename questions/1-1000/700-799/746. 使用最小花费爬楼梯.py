# Date:       2020/12/21
# encode:      UTF-8
__author__ = "zcTresure"

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(2, len(cost)):
            cost[i] = cost[i] + min(cost[i - 1], cost[i - 2])
        return cost[-1]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = curr = 0
        for i in range(2, len(cost) + 1):
            minCost = min(prev + cost[i - 2], curr + cost[i - 1])
            prev, curr = curr, minCost
        return curr


cost = [0, 0, 0, 0]
test = Solution()
print(test.minCostClimbingStairs(cost))
