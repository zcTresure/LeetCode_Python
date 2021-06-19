# -*- coding: utf-8 -*-
# File:     1239. 串联字符串的最大长度.py
# Date:     2021/6/19
# Software: PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = []
        for s in arr:  # 遍历所有字符串
            mask = 0
            for c in s:  # 遍历当前字符串字符
                idx = ord(c) - ord('a')
                if ((mask >> idx) & 1):  # 若 mask 已有 c，则说明 s 含有重复字母，无法构成可行解
                    mask = 0  # 当前字符串跳过
                    break
                mask |= (1 << idx)  # 将 c 加入 mask 中
            if mask > 0:  # s 没有重复字符
                masks.append(mask)
        ans = 0

        def backtrack(pos: int, mask: int) -> None:
            if pos == len(masks):
                nonlocal ans
                ans = max(ans, bin(mask).count('1'))
                return
            if (mask & masks[pos]) == 0:  # mask 和 masks[pos]无公共元素
                backtrack(pos + 1, mask | masks[pos])
            backtrack(pos + 1, mask)

        backtrack(0, 0)
        return ans


arr = ["un", "iq", "ue"]
print(Solution().maxLength(arr))
