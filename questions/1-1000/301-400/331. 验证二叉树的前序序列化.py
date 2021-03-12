# Date:       2021/3/12
# Coding:      UTF-8
__author__ = "zcTresure"


class Solution:
    # 栈
    def isValidSerialization(self, preorder: str) -> bool:
        stack = [1]
        n, i = len(preorder), 0
        while i < n:
            if not stack:
                return False
            if preorder[i] == ',':
                i += 1
            elif preorder[i] == '#':
                stack[-1] -= 1
                if stack[-1] == 0:
                    stack.pop()
                i += 1
            else:
                while i < n and preorder[i] != ',':
                    i += 1
                stack[-1] -= 1
                if stack[-1] == 0:
                    stack.pop()
                stack.append(2)
        return not stack

    # 计数
    def isValidSerialization(self, preorder: str) -> bool:
        stack = 1
        n, i = len(preorder), 0
        while i < n:
            if stack == 0:
                return False
            if preorder[i] == ',':
                i += 1
            elif preorder[i] == '#':
                stack -= 1
                i += 1
            else:
                while i < n and preorder[i] != ',':
                    i += 1
                stack += 1
            print(stack)
        return stack == 0


# preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
# preorder = "1,#"
preorder = "9,#,92,#,#"
test = Solution()
print(test.isValidSerialization(preorder))
