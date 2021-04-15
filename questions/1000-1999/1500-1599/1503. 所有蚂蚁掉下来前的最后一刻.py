class Solution:
    def getLastMoment(self, n: int, left: list, right: list) -> int:
        lastMoment = 0 if not left else max(left)
        if right:
            lastMoment = max(lastMoment,n-min(right))
        return lastMoment


n = 4
left = []
right = []
test = Solution()
print(test.getLastMoment(n, left, right))
