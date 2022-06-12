# -*- coding: utf-8 -*-
# File:      926. 将字符串翻转到单调递增.py
# DATA:      2022/6/12
# Software:  PyCharm
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp0 = dp1 = 0
        for c in s:
            dp0_new, dp1_new = dp0, min(dp0, dp1)
            if c == '1':
                dp0_new += 1
            else:
                dp1_new += 1
            dp0, dp1 = dp0_new, dp1_new
        return min(dp0, dp1)


print(Solution().minFlipsMonoIncr(s="00110"))
print(Solution().minFlipsMonoIncr(s="010110"))
print(Solution().minFlipsMonoIncr(s="00011000"))
