# -*- coding: utf-8 -*-
# File:    1763. 最长的美好子字符串.py
# Date:    2022/2/14
# Software: Pycharm
__author__ = 'zcFang'


class Solution:
    # 枚举
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        max_pos, max_len = 0, 0
        for i in range(n):
            lower, upper = 0, 0
            for j in range(i, n):
                if s[j].islower():
                    lower |= 1 << (ord(s[j]) - ord('a'))
                else:
                    upper |= 1 << (ord(s[j]) - ord('A'))
                if lower == upper and j - i + 1 > max_len:
                    max_pos, max_len = i, j - i + 1
        return s[max_pos:max_pos + max_len]

    # 分治
    def longestNiceSubstring(self, s: str) -> str:
        max_pos, max_len = 0, 0

        def dfs(start: int, end: int) -> None:
            nonlocal max_len, max_pos
            if start >= end:
                return
            lower, upper = 0, 0
            for i in range(start, end + 1):
                if s[i].islower():
                    lower |= 1 << (ord(s[i]) - ord('a'))
                else:
                    upper |= 1 << (ord(s[i]) - ord('A'))
            if lower == upper:
                if end - start + 1 > max_len:
                    max_pos, max_len = start, end - start + 1
                return
            pos, valid = start, lower & upper
            while pos <= end:
                start = pos
                while pos <= end and valid & (1 << (ord(s[pos].lower()) - ord('a'))):
                    pos += 1
                dfs(start, pos - 1)
                pos += 1

        dfs(0, len(s) - 1)
        return s[max_pos: max_pos + max_len]

    # 滑动窗口
    def longestNiceSubstring(self, s: str) -> str:
        def check(typeNum):
            nonlocal maxPos, maxLen
            lowerCnt = [0] * 26
            upperCnt = [0] * 26
            l, r, total, cnt = 0, 0, 0, 0
            while r < len(s):
                idx = ord(s[r].lower()) - ord('a')
                if s[r].islower():
                    lowerCnt[idx] += 1
                    if lowerCnt[idx] == 1 and upperCnt[idx] > 0:
                        cnt += 1
                else:
                    upperCnt[idx] += 1
                    if upperCnt[idx] == 1 and lowerCnt[idx] > 0:
                        cnt += 1
                if lowerCnt[idx] + upperCnt[idx] == 1:
                    total += 1

                while total > typeNum:
                    idx = ord(s[l].lower()) - ord('a')
                    if lowerCnt[idx] + upperCnt[idx] == 1:
                        total -= 1
                    if s[l].islower():
                        lowerCnt[idx] -= 1
                        if lowerCnt[idx] == 0 and upperCnt[idx] > 0:
                            cnt -= 1
                    else:
                        upperCnt[idx] -= 1
                        if upperCnt[idx] == 0 and lowerCnt[idx] > 0:
                            cnt -= 1
                    l += 1
                if cnt == typeNum and r - l + 1 > maxLen:
                    maxPos, maxLen = l, r - l + 1
                r += 1

        maxPos, maxLen = 0, 0
        types = len(set(s.lower()))
        for i in range(1, types + 1):
            check(i)
        return s[maxPos: maxPos + maxLen]


print(Solution().longestNiceSubstring(s="YazaAay"))
