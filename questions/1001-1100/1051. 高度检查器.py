class Solution:
    def heightChecker(self, heights):
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))


heights = [5, 1, 2, 3, 4]
test = Solution()
print(test.heightChecker(heights))
