# File Name:  28. 实现 strStr()
# date:       2021/4/20
# encode:      UTF-8
__author__ = 'zcTresure'


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def getNext(needle):
            n = len(needle)
            next = [0] * n
            j = 0
            for i in range(1, n):
                while j > 0 and needle[i] != needle[j]:
                    j = next[j - 1]
                if needle[i] == needle[j]:
                    j += 1
                next[i] = j
            return next

        def kmp(haystack, needle, next):
            if not needle: return 0
            m, n = len(haystack), len(next)
            if m < n: return -1
            j = 0
            for i in range(m):
                while j > 0 and haystack[i] != needle[j]:
                    j = next[j - 1]
                if haystack[i] == needle[j]:
                    j += 1
                if j == n:
                    return i - n + 1
            return -1

        next = getNext(needle)
        return kmp(haystack, needle, next)


haystack = "mississippi"
needle = "pi"
test = Solution()
print(test.strStr(haystack, needle))
