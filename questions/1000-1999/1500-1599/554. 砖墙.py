# -*- coding: utf-8 -*-
# File:     554. 砖墙
# Date:     2021/7/2
# Software: Pycharm
__author__ = 'zcFang'

from collections import defaultdict
from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        prefixSum = defaultdict(int)
        n = len(wall)
        for i in range(0, n):
            currSum = 0
            # 每一行砖的最后一列不要计算进来, 否则会把最右侧的垂直线考虑进去
            for j in range(0, len(wall[i]) - 1):
                # 计算每一行的砖的宽度和
                currSum += wall[i][j]
                # 如果有相同的前缀和, 这里会+1
                prefixSum[currSum] += 1
        # 总高度 减去 前缀和数量最多的
        return n - max(prefixSum.values(), default=0)


wall = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
print(Solution().leastBricks(wall))
