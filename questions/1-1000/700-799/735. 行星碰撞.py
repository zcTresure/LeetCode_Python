# -*- coding: utf-8 -*-
# File:    735. 行星碰撞.py
# Date:    2022/7/15
# Software: Pycharm
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for aster in asteroids:
            alive = True
            while alive and aster < 0 and st and st[-1] > 0:
                alive = st[-1] < -aster
                if st[-1] <= -aster:
                    st.pop()
            if alive:
                st.append(aster)
        return st


print(Solution().asteroidCollision(asteroids=[5, 10, -5]))
