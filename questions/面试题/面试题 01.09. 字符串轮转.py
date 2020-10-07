class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        return s1 in (s2 + s2)


s1 = "aba"
s2 = "bab"
test = Solution()
print(test.isFlipedString(s1, s2))
