class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    if c == ')' and stack[-1] == '(':
                        stack.pop()
                    elif c == ']' and stack[-1] == '[':
                        stack.pop()
                    elif c == '}' and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
        return not stack


class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        cmp = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in cmp:
                if not stack or stack[-1] != cmp[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack


s = "()[]{)}"
test = Solution()
print(test.isValid(s))
