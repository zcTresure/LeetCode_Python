# File Name:  面试题 17.21. 直方图的水量
# date:       2021/4/2
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List


class Solution:
    # 动态规划
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        left_max = [height[0]] + [0] * (n - 1)  # 从左向右看的三视图
        right_max = [0] * (n - 1) + [height[n - 1]]  # 从右向左看的三视图
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])  # 从左向右判断最大值并更新
            right_max[n - i - 1] = max(right_max[n - i], height[n - i - 1])  # 从右向左判断最大值并更新
        # 下标 i 处能接的水的量等于 min(leftMax[i], rightMax[i]) − height[i]
        return sum(min(left_max[i], right_max[i]) - height[i] for i in range(n))

    # 单调栈
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []
        n = len(height)
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()  # 水池中间高度
                if not stack: break
                left = stack[-1]  # 水池左侧高度
                cur_width = i - left - 1  # 水池凹槽的宽度
                cur_height = min(height[left], h) - height[top]  # 水池左边和右边的最低高度减去水池中间高度就是水池的高度
                ans += cur_width * cur_height  # 累加水池容量
            stack.append(i)
        return ans

    # 双指针
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: return 0
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
