# -*- coding: utf-8 -*-
# File:      423. 从英文中重建数字.py
# DATA:      2021/11/24
# Software:  PyCharm
__author__ = 'zcFang'

from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        count = Counter(s)
        cnt = [0] * 10

        # 在数字中单独出现的字符
        cnt[0] = count['z']
        cnt[2] = count['w']
        cnt[4] = count['u']
        cnt[6] = count['x']
        cnt[8] = count['g']

        # 在数字中出现两次的字符
        cnt[3] = count['h'] - cnt[8]
        cnt[5] = count['f'] - cnt[4]
        cnt[7] = count['s'] - cnt[6]

        cnt[9] = count['i'] - cnt[5] - cnt[6] - cnt[8]
        cnt[1] = count['o'] - cnt[0] - cnt[2] - cnt[4]
        return "".join(str(x) * cnt[x] for x in range(10))


# s = "owoztneoer"
s = "fviefuro"
print(Solution().originalDigits(s))
