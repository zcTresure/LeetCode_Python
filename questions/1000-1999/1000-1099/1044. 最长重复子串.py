# -*- coding: utf-8 -*-
# File:      1044. 最长重复子串.py
# DATA:      2021/12/23
# Software:  PyCharm
__author__ = 'zcFang'

import random


class Solution:
    # 二分查找 + Rabin-Karp 字符串编码
    def longestDupSubstring(self, s: str) -> str:
        a1, a2 = random.randint(26, 100), random.randint(26, 100)  # 生成两个进制
        mod1, mod2 = random.randint(10 ** 9 + 7, 2 ** 31 - 1), random.randint(10 ** 9 + 7, 2 ** 31 - 1)  # 生成两个模
        n = len(s)
        arr = [ord(c) - ord('a') for c in s]  # 对所有字符串进行编码
        left, right = 1, n - 1 # 二分查找的范围
        length, start = 0, -1
        while left <= right:
            mid = left + (right - left + 1) // 2
            idx = self.check(arr, mid, a1, a2, mod1, mod2)
            if idx != -1:  # 有重复子串， 移动左边界
                left = mid + 1
                length = mid
                start = idx
            else:  # 无重复子串，移动右边界
                right = mid - 1
        return s[start:start + length] if start != -1 else ""

    def check(self, arr: list, mid: int, a1: int, a2: int, mod1: int, mod2: int) -> int:
        n = len(arr)
        a_l1, a_l2 = pow(a1, mid, mod1), pow(a2, mid, mod2)
        h1, h2 = 0, 0
        for i in range(mid):
            h1 = (h1 * a1 + arr[i]) % mod1
            h2 = (h2 * a2 + arr[i]) % mod2
        seen = {(h1, h2)}  # 存储一个编码组合是否出现过
        for start in range(1, n - mid + 1):
            h1 = (h1 * a1 - arr[start - 1] * a_l1 + arr[start + mid - 1]) % mod1
            h2 = (h2 * a2 - arr[start - 1] * a_l2 + arr[start + mid - 1]) % mod2
            if (h1, h2) in seen:  # 如果有重复，则返回重复串的起点
                return start
            seen.add((h1, h2))
        return -1  # 没有重复，返回-1


s = "abcababa"
print(Solution().longestDupSubstring(s))
