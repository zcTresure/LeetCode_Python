# File Name:  面试题 17.21. 直方图的水量
# date:       2021/4/2
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List


class Solution:
    # 双指针
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        water = 0
        left, right = 0, len(height) - 1  # 左右两个指针
        left_max, right_max = height[left], height[right]
        while left < right:  # 每次根据左右两边较低的柱体判断
            if left_max < right_max:
                water += left_max - height[left]  # 左侧最高减去当前的高度，就是当前位置可以储存的水量
                left += 1  # 左指针向右移动
                left_max = max(left_max, height[left])  # 更新左侧最高值
            else:
                water += right_max - height[right]  # 右侧最高减去当前的高度，就是当前位置可以储存的水量
                right -= 1  # 右指针向左移动
                right_max = max(right_max, height[right])  # 更新右侧最高值
        return water


test = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(test.trap(height))
