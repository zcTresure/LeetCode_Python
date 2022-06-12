# -*- coding: utf-8 -*-
# File:      1790. 仅执行一次字符串交换能否使两个字符串相等.py
# DATA:      2022/6/10
# Software:  PyCharm
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        cnt = 0
        c1 = c2 = c3 = c4 = ''
        for x, y in zip(s1, s2):
            if x != y:
                cnt += 1
                c1, c2 = x, c1
                c3, c4 = y, c3
        return cnt == 0 or (cnt == 2 and c1 == c4 and c2 == c3)


print(Solution().areAlmostEqual(s1="bank", s2="kanb"))
print(Solution().areAlmostEqual(s1="attack", s2="defend"))
print(Solution().areAlmostEqual(s1="kelb", s2="kelb"))
print(Solution().areAlmostEqual(s1="abcd", s2="dcba"))
