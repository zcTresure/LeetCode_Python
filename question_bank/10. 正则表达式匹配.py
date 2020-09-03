# 先判断s和p的第一个字符是否匹配
# 处理p[1]为*号的情况：匹配0个或多个字符
# 处理.号的情况：匹配一个字符
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:                                       # 结束条件
            return not s
        fist_match = len(s) > 0 and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':                 # 先处理 *
            return self.isMatch(s, p[2:]) or (fist_match and self.isMatch(s[1:], p))
        return fist_match and self.isMatch(s[1:], p[1:])  # 处理首字母匹配

    def isMatch(self, s: str, p: str) -> bool:
        def recur(i, j):
            # 结束条件
            if j == len(p):
                return i == len(s)
            # 首字母匹配
            first_match = (len(s) > i) and (p[j] == s[i] or p[j] == '.')
            # 处理 `*`
            if len(p) >= j + 2 and p[j + 1] == '*':
                return recur(i, j + 2) or (first_match and recur(i + 1, j))
            # 处理首字母匹配
            return first_match and recur(i + 1, j + 1)
        return recur(0, 0)

    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matchs(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]
        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matchs(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matchs(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]


s = "aa"
p = "a*"
test = Solution()
print(test.isMatch(s, p))
