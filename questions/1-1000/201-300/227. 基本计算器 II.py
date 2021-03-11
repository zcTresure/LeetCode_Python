# Date:       2021/3/11
# Coding:      UTF-8
__author__ = "zcTresure"


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        s += '#'
        preChar = '+'
        for c in s:
            if c == ' ':
                continue
            elif c.isdigit():

                num = num * 10 + int(c)
            else:
                if preChar == '+':
                    stack.append(num)
                elif preChar == '-':
                    stack.append(-num)
                elif preChar == '*':
                    stack.append(stack.pop() * num)
                elif preChar == '/':
                    stack.append(int(stack.pop() / num))
                num = 0
                preChar = c
        return sum(stack)


test = Solution()
s = "14-3/2"
print(test.calculate(s))
