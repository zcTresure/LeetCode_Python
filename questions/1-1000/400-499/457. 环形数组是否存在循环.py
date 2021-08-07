# -*- coding: utf-8 -*-
# File:      457. 环形数组是否存在循环.py
# DATA:      2021/8/7
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    @classmethod
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next(cur: int) -> int:
            return (cur + nums[cur]) % n  # 防止下标越界

        for i, num in enumerate(nums):
            if nums[i] == 0: continue  # 碰到元素零直接跳过
            slow, fast = i, next(i)

            # 判断非零而且方向相同
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[next(fast)] > 0:
                if slow == fast:
                    if slow == next(slow):
                        break
                    return True
                slow = next(slow)
                fast = next(next(fast))

            add = i
            # 遍历过的元素不是环的置零，防止重复搜索
            while nums[add] * nums[next(add)] > 0:
                tmp = add
                add = next(add)
                nums[tmp] = 0

        return False


if __name__ == '__main__':
    nums = [2, -1, 1, 2, 2]
    print(Solution.circularArrayLoop(nums))
