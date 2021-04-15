class Solution:
    # DFS
    def checkValidString(self, s: str) -> bool:
        def check(s: str, count: int) -> bool:
            if count < 0:
                return False
            for i in range(len(s)):
                c = s[i]
                if c == '(':
                    count += 1
                elif c == ')':
                    if count == 0:
                        return False
                    count -= 1
                else:
                    return check(s[i + 1:], count + 1) or check(s[i + 1:], count - 1) or check(s[i + 1:], count)
            return count == 0

        return check(s, 0)

    # 贪心
    def checkValidString(self, s: str) -> bool:
        # 维护当前左括号的数量范围在[minLeft, maxLeft]
        minLeft, maxLeft = 0, 0
        for c in s:
            if c == '(':
                minLeft += 1
                maxLeft += 1
            elif c == ')':
                minLeft -= 1 if minLeft > 0 else 0
                # 左括号不够了
                if maxLeft == 0:
                    return False
                maxLeft -= 1
            else:
                # 作为右括号，与左括号抵消
                minLeft -= 1 if minLeft > 0 else 0
                # 作为左括号
                maxLeft += 1
        return minLeft == 0


s = '((()))'
test = Solution()
print(test.checkValidString(s))
