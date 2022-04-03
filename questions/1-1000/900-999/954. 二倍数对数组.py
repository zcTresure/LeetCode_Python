# -*- coding: utf-8 -*-
# File:      954. 二倍数对数组.py
# DATA:      2022/4/1
# Software:  PyCharm
__author__ = 'zcFang'

from collections import Counter
from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        for num in sorted(cnt, key=abs):
            if cnt[2 * num] < cnt[num]:
                return False
            cnt[2 * num] -= cnt[num]
        return True


# arr = [1, 3, 3, 1]
arr = [2, 4, - 2, - 4]
print(Solution().canReorderDoubled(arr))
