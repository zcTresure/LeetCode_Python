# -*- coding: utf-8 -*-
# File:      68. 文本左右对齐.py
# DATA:      2021/9/9
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def blank(self, n: int) -> str:
        return ' ' * n

    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        right, n, = 0, len(words)
        ans = list()
        while True:
            left = right
            sum_len = 0
            while right < n and sum_len + len(words[right]) + right - left <= max_width:
                sum_len += len(words[right])
                right += 1
            if right == n:
                s = ' '.join(words[left:])
                ans.append(s + self.blank(max_width - len(s)))
                break
            new_words = right - left
            new_space = max_width - sum_len
            if new_words == 1:
                ans.append(''.join(words[left]) + self.blank(max_width - len(words[left])))
                continue
            avg_space = new_space // (new_words - 1)
            extra_space = new_space % (new_words - 1)
            s1 = self.blank(avg_space + 1).join(words[left:left + extra_space + 1])
            s2 = self.blank(avg_space).join(words[left + extra_space + 1:right])
            ans.append(s1 + self.blank(avg_space) + s2)

        return ans


words = ["What", "must", "be", "acknowledgment", "shall", "be"]
maxWidth = 16
print(Solution().fullJustify(words, maxWidth))
