# File Name:  90. 子集 II
# date:       2021/3/31
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def recur(num, path):
            res.append(path[:])
            if len(num) == 0: return
            for i in range(len(num)):
                # 同一组可以出现相同的元素，但是不能出现相同的组
                if i > 0 and num[i] == num[i - 1]:
                    continue
                path.append(num[i])
                recur(num[i + 1:], path)
                path.pop()

        nums.sort()
        recur(nums, [])
        return res


nums = [1, 2, 2]
test = Solution()
print(test.subsetsWithDup(nums))
