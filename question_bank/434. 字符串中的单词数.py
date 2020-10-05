class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())


s = "Hello, my name is ZC"
test = Solution()
print(test.countSegments(s))