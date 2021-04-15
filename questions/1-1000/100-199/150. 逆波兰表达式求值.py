# File Name:  150. 逆波兰表达式求值
# date:       2021/3/20
# oding:      UTF-8
__author__ = 'zcTresure'

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                stack.append((stack.pop() + stack.pop()))
            elif tokens[i] == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b - a))
            elif tokens[i] == '*':
                stack.append(stack.pop() * stack.pop())
            elif tokens[i] == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(tokens[i]))
            print(stack)
        return stack[-1]


test = Solution()
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(test.evalRPN(tokens))
