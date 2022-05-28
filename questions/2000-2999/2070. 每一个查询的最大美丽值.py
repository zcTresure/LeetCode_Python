# -*- coding: utf-8 -*-
# File:      2070. 每一个查询的最大美丽值.py
# DATA:      2022/5/28
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # 物品按照价格升序排列
        items.sort(key=lambda x: x[0])
        n = len(items)
        # 根据定义修改美丽值
        for i in range(1, n):
            items[i][1] = max(items[i - 1][1], items[i][1])
        print(items)

        # 二分查找
        def quarry(q: int) -> int:
            left, right = 0, len(items)
            while left < right:
                mid = (right - left) // 2 + left
                if items[mid][0] > q:
                    right = mid
                else:
                    left = mid + 1
            if left == 0:
                # 所有物品价格均大于查询价格
                return 0
            else:
                # 返回魅力值等于查询价格的最大美丽值
                return items[left - 1][1]

        res = [quarry(q) for q in queries]
        return res


print(Solution().maximumBeauty(items=[[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], queries=[1, 2, 3, 4, 5, 6]))
