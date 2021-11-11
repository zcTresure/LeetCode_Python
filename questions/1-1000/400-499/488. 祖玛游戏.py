# -*- coding: utf-8 -*-
# File:      488. 祖玛游戏.py
# DATA:      2021/11/9
# Software:  PyCharm
__author__ = 'zcFang'

from collections import Counter
from functools import lru_cache
from typing import re

COLORS = ["R", "Y", "B", "G", "W"]


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        # 单纯检测一下board里有没有加上手上的还不能够3个的球，直接返回-1
        cnts, cnts_b = Counter(hand), Counter(board)
        total = len(hand)
        if any(cnts_b[k] + cnts[k] < 3 for k in cnts_b.keys()):
            return -1

        @lru_cache(None)
        def dfs(bd, hd):
            # 全部消掉了，返回所用的球数
            if len(bd) <= 0:
                return total - sum(hd)
            n = len(bd)
            ans = float("inf")
            # 遍历手上的球的颜色
            for i, v in enumerate(hd):
                # 如果该颜色还有球可以用
                if v:
                    cp = list(hd)
                    # 用掉这个球
                    cp[i] -= 1
                    nt = tuple(cp)
                    # 枚举插入位置
                    for j in range(n + 1):
                        ans = min(ans, dfs(in_a_row(bd[:j] + COLORS[i] + bd[j:]), nt))
            return ans

        @lru_cache(None)
        def in_a_row(bd):
            l = r = 0
            while l < len(bd):
                # 判断有没有连续三个一样的球，有的话就剪掉bd[l:r]，迭代返回
                while r < len(bd) and bd[r] == bd[l]:
                    r += 1
                if r - l > 2:
                    return in_a_row(bd[:l] + bd[r:])
                l = r
            return bd

        # 手上的以不同颜色的球计数的tuple作为传参，直接避免尝试重复的球
        start = [cnts[c] for c in COLORS]
        res = dfs(board, tuple(start))
        return res if res != float("inf") else -1

    def findMinStep(self, board: str, hand: str) -> int:
        def clean(s):
            # 消除桌面上需要消除的球
            n = 1
            while n:
                s, n = re.subn(r"(.)\1{2,}", "", s)
            return s

        cnts = Counter(hand)
        start = [cnts[c] for c in COLORS]
        hand = tuple(start)

        # 初始化用双端队列维护的状态队列：其中的三个元素分别为当前桌面的球、当期手中的球、当前回合数
        queue = deque([(board, hand, 0)])

        # 记忆化
        visited = {(board, hand)}

        while queue:
            cur_board, cur_hand, step = queue.popleft()
            for i in range(len(cur_board) + 1):
                for j in range(len(cur_hand)):
                    if not cur_hand[j]:
                        continue
                    c = COLORS[j]
                    # 第 1 个剪枝条件: 只在连续相同颜色的球的开头位置插入新球(在它前面插入过了，不需要再插入，意义相同)
                    if i > 0 and cur_board[i - 1] == c:
                        continue

                    # 第 2 个剪枝条件: 只在以下两种情况放置新球
                    #  - 第 1 种情况 : 当前后颜色相同且与当前颜色不同时候放置球
                    #  - 第 2 种情况 : 当前球颜色与后面的球的颜色相同
                    choose = False
                    if 0 < i < len(cur_board) and cur_board[i - 1] == cur_board[i] and cur_board[i - 1] != c:
                        choose = True
                    if i < len(cur_board) and cur_board[i] == c:
                        choose = True

                    if choose:
                        cp = list(cur_hand)
                        cp[j] -= 1
                        b2, h2 = clean(cur_board[:i] + c + cur_board[i:]), tuple(cp)
                        if not b2:
                            return step + 1
                        if (b2, h2) not in visited:
                            queue.append((b2, h2, step + 1))
                            visited.add((b2, h2))

        return -1


board = "WRRBBW"
hand = "WRB"
print(Solution().findMinStep(board, hand))
