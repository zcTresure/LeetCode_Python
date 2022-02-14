# -*- coding: utf-8 -*-
# File:    1996. 游戏中弱角色的数量.py
# Date:    2022/2/14
# Software: Pycharm
__author__ = 'zcFang'

from typing import List


class Solution:
    # 排序
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        ans = 0
        maxDef = 0
        for _, def_ in properties:
            if maxDef > def_:
                ans += 1
            else:
                maxDef = max(maxDef, def_)
        return ans

    # 单调栈
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))
        ans = 0
        st = []
        for _, mass in properties:
            while st and st[-1] < mass:
                st.pop()
                ans += 1
            st.append(mass)
        return ans


print(Solution().numberOfWeakCharacters(properties=[[5, 5], [6, 3], [3, 6]]))
