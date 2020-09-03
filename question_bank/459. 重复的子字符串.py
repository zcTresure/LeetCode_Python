class Solution:
    # 暴力枚举
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                if all(s[j] == s[j - i] for j in range(i, n)):
                    return True
        return False

    # 字符串匹配
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)

    # KMP
    def repeatedSubstringPattern(self, s: str) -> bool:
        def kmp(ss: str, s: str) -> bool:
            n, m = len(ss), len(s)
            fail = [-1] * m
            for i in range(1, m):
                j = fail[i - 1]
                while j != -1 and s[j + 1] != s[i]:
                    j = fail[j]
                if s[j + 1] == s[i]:
                    fail[i] = j + 1
            tmp = -1
            for i in range(1, n - 1):
                while tmp != -1 and s[tmp + 1] != ss[i]:
                    tmp = fail[tmp]
                if s[tmp + 1] == ss[i]:
                    tmp += 1
                    if tmp == m - 1:
                        return True
            return False
        return kmp(s + s, s)

    # KMP优化
    def repeatedSubstringPattern(self, s: str) -> bool:
        def kmp(ss: str) -> bool:
            n, m = len(ss), len(s)
            fail = [-1] * m
            for i in range(1, m):
                j = fail[i - 1]
                while j != -1 and s[j + 1] != s[i]:
                    j = fail[j]
                if s[j + 1] == s[i]:
                    fail[i] = j + 1
            return fail[n - 1] != -1 and n % (n - fail[n - 1] - 1) == 0
        return kmp(s)


s = "abab"
test = Solution()
print(test.repeatedSubstringPattern(s))
