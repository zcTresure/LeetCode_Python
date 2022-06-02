# -*- coding: utf-8 -*-
# File:      1456. 定长子串中元音的最大数目.py
# DATA:      2022/5/29
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    # 记忆化数组
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        cnt = [0] * (n + 1)
        for i in range(len(s)):
            if s[i] in "aeiou":
                cnt[i + 1] = cnt[i] + 1
            else:
                cnt[i + 1] = cnt[i]
        max_cnt = 0
        for i in range(0, n - k + 1):
            max_cnt = max(max_cnt, cnt[k + i] - cnt[i])
        return min(k, max_cnt)

    # 滑动窗口
    def maxVowels(self, s: str, k: int) -> int:
        ans = 0
        dic = "aeiou"
        cnt = sum(1 for i in range(k) if s[i] in dic)
        for i in range(k, len(s)):
            cnt += (s[i] in dic) - (s[i - k] in dic)
            ans = max(ans, cnt)
        return ans


print(Solution().maxVowels(s="abciiidef", k=3))
print(Solution().maxVowels(s="aeiou", k=2))
print(Solution().maxVowels(s="leetcode", k=3))
print(Solution().maxVowels(s="rhythms", k=4))
print(Solution().maxVowels(s="tryhard", k=4))
