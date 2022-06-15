# -*- coding: utf-8 -*-
# File:      1678. 设计 Goal 解析器.py
# DATA:      2022/6/15
# Software:  PyCharm
class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        cnt = 1
        for c in command:
            if c == '(':
                cnt = 1
            elif c == ')':
                if cnt == 1:
                    ans = ans + 'o'
            else:
                cnt = 0
                ans = ans + c
        return ans


print(Solution().interpret(command="G()(al)"))
print(Solution().interpret(command="G()()()()(al)"))
print(Solution().interpret(command="(al)G(al)()()G"))
