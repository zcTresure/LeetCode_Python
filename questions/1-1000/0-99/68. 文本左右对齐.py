# -*- coding: utf-8 -*-
# File:      68. 文本左右对齐.py
# DATA:      2021/9/9
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    # 返回长度为 n 的由空格组成的字符串
    def blank(self, n: int) -> str:
        return ' ' * n

    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        right, n, = 0, len(words)
        ans = list()
        while True:
            left = right  # 当前行的第一个单词在words的位置
            sum_len = 0  # 当前行单词的总长度
            # 循环确定当前行能放多少个单词，单词之间必须由一个空格
            while right < n and sum_len + len(words[right]) + right - left <= max_width:
                sum_len += len(words[right])
                right += 1

            # 当前行为最后一行：单词左对齐，且单词间有一个空格，并在行末填充空格
            if right == n:
                s = ' '.join(words[left:])
                ans.append(s + self.blank(max_width - len(s)))
                break
            new_words = right - left  # 新单词数量
            new_space = max_width - sum_len  # 剩余空格长度

            # 当前行只有一个单词：单词左对齐，在行末填充空格
            if new_words == 1:
                ans.append(''.join(words[left]) + self.blank(max_width - len(words[left])))
                continue

            # 当前行不止一个单词
            avg_space = new_space // (new_words - 1)  # 单词间的平均空格数
            extra_space = new_space % (new_words - 1)  # 剩余空格靠前放置
            s1 = self.blank(avg_space + 1).join(words[left:left + extra_space + 1])
            s2 = self.blank(avg_space).join(words[left + extra_space + 1:right])
            ans.append(s1 + self.blank(avg_space) + s2)

        return ans


words = ["What", "must", "be", "acknowledgment", "shall", "be"]
maxWidth = 16
print(Solution().fullJustify(words, maxWidth))
