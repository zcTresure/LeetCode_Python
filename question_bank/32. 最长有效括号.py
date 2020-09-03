# 栈
# def longestValidParentheses(self, s: str) -> int:
#     ans = 0
#     stack = [-1, ]
#     for i, ch in enumerate(s):
#         if ch == '(':
#             stack.append(i)
#         elif len(stack) > 1:
#             stack.pop()
#             ans = max(ans, i - stack[-1])
#         else:
#             stack[0] = i
#     return ans

# 贪心
def longestValidParentheses(self, s: str) -> int:
    logest = left = right = 0
    for i in range(len(s)):
        if s[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            logest = max(logest, 2 * left)
        elif right > left:
            left = right = 0
    print(logest)
    left = right = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            logest = max(logest, 2 * left)
        elif right < left:
            left = right = 0
    return logest


s = "(()"
print(longestValidParentheses(1, s))
