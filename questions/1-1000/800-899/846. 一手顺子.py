# -*- coding: utf-8 -*-
# File:      846. 一手顺子.py
# DATA:      2021/12/30
# Software:  PyCharm
__author__ = 'zcFang'

from collections import defaultdict, Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        cnt = Counter(hand)
        for Lnum in hand:
            if cnt[Lnum] == 0:
                continue
            for Rnum in range(Lnum, Lnum + groupSize):
                if cnt[Rnum] == 0:
                    return False
                cnt[Rnum] -= 1
        return True


hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3
print(Solution().isNStraightHand(hand, groupSize))
