# -*- coding: utf-8 -*-
# File:      799. 香槟塔.py
# DATA:      2021/9/10
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # 压缩dp数组
        dp = [0.0] * (query_glass + 2)
        dp[0] = poured
        for i in range(query_row):  # 层数遍历，一层层的往下流
            for j in range(min(i, query_glass), -1, -1):  # 倒序遍历，避免香槟影响上一轮结果
                dp[j], v = 0.0, dp[j]
                if (v > 1):  # 上一层体积大于1的液体分流，否则下层为0
                    dp[j] += (v - 1) / 2  # 上一层的下层左边杯子
                    dp[j + 1] += (v - 1) / 2  # 上一层的下层的右边被子
        return min(1.0, dp[query_glass])


print(Solution().champagneTower(100000009, 33, 17))
