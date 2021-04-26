# File Name:  1011. 在 D 天内送达包裹的能力
# date:       2021/4/26
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        # 确定二分查找左右边界
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (right - left) // 2 + left
            need, cur = 1, 0  # 所需天数，当前重量
            for weight in weights:
                if cur + weight > mid:  # 判断重量，重量超过mid 当前重量归零，天数加一
                    need += 1
                    cur = 0
                cur += weight
            if need <= D:
                right = mid
            else:
                left = mid + 1
        return left


weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
D = 5
test = Solution()
print(test.shipWithinDays(weights, D))
