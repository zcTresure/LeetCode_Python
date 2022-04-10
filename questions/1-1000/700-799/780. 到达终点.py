# -*- coding: utf-8 -*-
# File:      780. 到达终点.py
# DATA:      2022/4/9
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    # 辗转相除
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx > sx and ty > sy:  # 约束tx ty 等于或小于 sx sy
            tx, ty = (tx % ty, ty) if tx > ty else (tx, ty % tx)

        return (tx == sx and ty >= sy and not (ty - sy) % sx) or (ty == sy and tx >= sx and not (tx - sx) % sy)


print(Solution().reachingPoints(sx=1, sy=1, tx=3, ty=5))
print(Solution().reachingPoints(sx=1, sy=1, tx=2, ty=2))
print(Solution().reachingPoints(sx=1, sy=1, tx=1, ty=1))
