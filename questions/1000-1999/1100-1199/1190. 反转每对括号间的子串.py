# -*- coding: utf-8 -*-
# File:     1190. 反转每对括号间的子串.py
# Date:     2021/5/26
# Software: PyCharm
__author__ = 'zcFang'

from collections import deque


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ')':
                stack.append(c)
            if c == ')':
                tmp = []
                while stack and stack[-1] != '(':
                    tmp.append(stack.pop())
                stack.pop()
                stack += tmp
        return ''.join(stack)

    def reverseParentheses(self, s: str) -> str:
        stack = []
        n = len(s)
        tmp = [0] * n
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            if s[i] == ')':
                j = stack.pop()
                tmp[i] = j
                tmp[j] = i
        index, step = 0, 1
        ans = []
        while index < n:
            if s[index] == '(' or s[index] == ')':
                index = tmp[index]
                step = -step
            else:
                ans.append(s[index])
            index += step
            print(index)
        return "".join(ans)


s = "(ed(et(oc))el)"
test = Solution()
print(test.reverseParentheses(s))
