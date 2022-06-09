# -*- coding: utf-8 -*-
# File:      365. 水壶问题.py
# DATA:      2022/6/7
# Software:  PyCharm
from math import gcd


class Solution:
    # 深度优先搜索
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        stack = [(0, 0)]
        seen = set()
        while stack:
            remain_x, remain_y = stack.pop()
            if remain_x == targetCapacity or remain_y == targetCapacity or remain_x + remain_y == targetCapacity:
                return True
            if (remain_x, remain_y) in seen:
                continue
            seen.add((remain_x, remain_y))
            stack.append((jug1Capacity, remain_y))  # 把第一个壶灌满
            stack.append((remain_x, jug2Capacity))  # 把第二个壶灌满
            stack.append((0, remain_y))  # 把第一个壶倒空
            stack.append((remain_x, 0))  # 把第二个壶倒空
            # 把第一个壶的水倒入第二个壶
            stack.append(
                (remain_x - min(remain_x, jug2Capacity - remain_y), remain_y + min(remain_x, jug2Capacity - remain_y)))
            # 把第二个壶的水倒入第一个壶
            stack.append(
                (remain_x + min(remain_y, jug1Capacity - remain_x), remain_y - min(remain_y, jug1Capacity - remain_x)))
        return False

    # 数学
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        if jug1Capacity == 0 or jug2Capacity == 0:
            return targetCapacity == 0 or jug1Capacity + jug2Capacity == targetCapacity
        return targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0


print(Solution().canMeasureWater(1, 2, 3))
print(Solution().canMeasureWater(2, 2, 3))
print(Solution().canMeasureWater(4, 2, 2))
