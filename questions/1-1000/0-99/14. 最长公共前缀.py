class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        for i, L in enumerate((*(len(set(t)) for t in zip(*strs)), 2)):
            if L > 1:
                return (*strs, "")[0][:i]


strs = ["flower", "flow", "flight"]
test = Solution()
print(test.longestCommonPrefix(strs))
