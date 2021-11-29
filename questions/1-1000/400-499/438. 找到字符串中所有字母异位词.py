# -*- coding: utf-8 -*-
# File:      438. 找到字符串中所有字母异位词.py
# DATA:      2020/09/16
# Software:  PyCharm
__author__ = 'zcFang'

from collections import Counter, defaultdict


class Solution:
    # 暴力迭代(时间超限)
    def findAnagrams(self, s: str, p: str) -> list:
        lenp = len(p)
        p = "".join(sorted(p))
        res = list()
        for i in range(len(s) - len(p) + 1):
            if "".join(sorted(s[i:i + lenp])) == p:
                res.append(i)
        return res

    # 暴力迭代 + 哈希优化（时间超限）
    def findAnagrams(self, s: str, p: str) -> list:
        res = list()
        lenp = len(p)
        dict_p = defaultdict(int)
        for c in p:
            dict_p[c] += 1
        for i in range(len(s) - lenp + 1):
            flag = True
            for c in p:
                if s[i:i + lenp].count(c) != dict_p[c]:
                    flag = False
                    break
            if flag:
                res.append(i)
        return res

    # 哈希 + 前缀和
    def findAnagrams(self, s: str, p: str) -> list:
        lens, lenp = len(s), len(p)
        res = list()
        p = Counter(p)
        prefix = [0] * (lens + 1)
        prefix[0] = Counter()
        for i in range(1, lens + 1):
            prefix[i] = prefix[i - 1].copy()
            prefix[i][s[i - 1]] += 1
            if i >= lenp and prefix[i] - prefix[i - lenp] == p:
                res.append(i - lenp)
        return res

    # 滑动窗口
    def findAnagrams(self, s: str, p: str) -> list:
        countP = [0] * 26
        countS = [0] * 26
        res = list()
        for c in p:
            countP[ord(c) - 97] += 1
        left = 0
        for right in range(len(s)):
            if right < len(p) - 1:
                countS[ord(s[right]) - 97] += 1
                continue
            countS[ord(s[right]) - 97] += 1
            if countP == countS:
                res.append(left)
            countS[ord(s[left]) - 97] -= 1
            left += 1
        return res

    # 优化滑动窗口
    def findAnagrams(self, s: str, p: str) -> list:
        s_len, p_len = len(s), len(p)
        ans = []
        if s_len < p_len:
            return ans
        count = [0] * 26
        for i in range(p_len):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(p[i]) - ord('a')] += 1

        differ = [c != 0 for c in count].count(True)
        if differ == 0:
            ans.append(0)

        for i in range(s_len - p_len):
            if count[ord(s[i]) - ord('a')] == 1:  # 窗口中字符s[i]的数量与字符串p的数量不同
                differ -= 1
            elif count[ord(s[i]) - ord('a')] == 0:  # 窗口中字符s[i]的数量与字符串p的数量相同
                differ += 1
            count[ord(s[i]) - ord('a')] -= 1

            if count[ord(s[i + p_len]) - ord('a')] == -1:  # 窗口中字符s[i-p_len]的数量与字符串p的数量不同
                differ -= 1
            elif count[ord(s[i + p_len]) - ord('a')] == 0:  # 窗口中字符s[i-p_len]的数量与字符串p的数量相同
                differ += 1
            count[ord(s[i + p_len]) - ord('a')] += 1

            if differ == 0:
                ans.append(i + 1)

        return ans


s = "cbaebabacd"
p = "abc"
test = Solution()
print(test.findAnagrams(s, p))
