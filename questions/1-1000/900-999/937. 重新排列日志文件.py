# -*- coding: utf-8 -*-
# File:      937. 重新排列日志文件.py
# DATA:      2022/5/4
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def trans(log: str) -> tuple:
            a, b = log.split(' ', 1)
            return (0, b, a) if b[0].isalpha() else (1,)

        logs.sort(key=trans)  # sort 是稳定排序
        return logs


print(
    Solution().reorderLogFiles(logs=["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))
