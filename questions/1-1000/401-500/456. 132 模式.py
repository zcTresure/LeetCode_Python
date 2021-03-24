# File Name:  456. 132 模式
# date:       2021/3/24
# Coding:      UTF-8
__author__ = 'zcTresure'

from typing import List
import bisect


class Solution:
    # 单调栈
    def find132pattern(self, nums: List[int]) -> bool:
        candidate_k = [nums[-1]]
        max_k = float('-inf')
        for i in range(len(nums) - 2, -1, -1):
            # 当前元素小于阈值，说明132模式已经找到，返回
            if nums[i] < max_k:
                # print(nums[i], candidate_k, max_k)
                return True
            # 将所有小于当前的元素移除，并更新阈值
            while candidate_k and nums[i] > candidate_k[-1]:
                max_k = candidate_k[-1]
                candidate_k.pop()
            # 将大于阈值的元素入栈
            if nums[i] > max_k:
                candidate_k.append(nums[i])
        return False

    # 单调栈 + 二分查找
    def find132pattern(self, nums: List[int]) -> bool:
        candidate_i, candidate_j = [-nums[0]], [-nums[0]]

        for v in nums[1:]:
            idx_i = bisect.bisect_right(candidate_i, -v)
            idx_j = bisect.bisect_left(candidate_j, -v)
            if idx_i < idx_j:
                return True

            if v < -candidate_i[-1]:
                candidate_i.append(-v)
                candidate_j.append(-v)
            elif v > -candidate_j[-1]:
                last_i = -candidate_i[-1]
                while candidate_j and v > -candidate_j[-1]:
                    candidate_i.pop()
                    candidate_j.pop()
                candidate_i.append(-last_i)
                candidate_j.append(-v)
        return False


nums = [3, 1, 4, 2]
test = Solution()
print(test.find132pattern(nums))
