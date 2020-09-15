class Solution:
    # 暴力迭代
    def maxArea(self, height: list) -> int:
        res = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                h = min(height[i], height[j])
                res = max(res, h * (j - i))
        return res

    # 双指针
    def maxArea(self, height: list) -> int:
        left, right, res = 0, len(height) - 1, 0
        while left <= right:
            # 将两边的杯壁高度进行比较，杯壁较矮的那一端进行更新
            if height[left] >= height[right]:
                res = max(res, height[right] * (right - left))
                right -= 1
            else:
                res = max(res, height[left] * (right - left))
                left += 1
            print(left, right, res)
        return res


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(height))
