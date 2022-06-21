# File Name:  150. 逆波兰表达式求值
# date:       2021/3/20
# oding:      UTF-8

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in '+-*/':
                a, b = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(b - a)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(b / a))
            else:
                stack.append(int(token))
        return stack[0]


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(Solution().evalRPN(tokens))
