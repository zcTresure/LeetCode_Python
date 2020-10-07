def trap(self, height: list) -> int:
    if len(height) < 3:
        return 0
    water = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    while left < right:
        if left_max < right_max:
            water += left_max - height[left]
            left += 1
            left_max = max(left_max, height[left])
        else:
            water += right_max - height[right]
            right -= 1
            right_max = max(right_max, height[right])
    return water


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(1, height))
