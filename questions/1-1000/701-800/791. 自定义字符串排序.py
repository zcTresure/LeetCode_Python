from collections import Counter


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        count = Counter(T)
        ans = []
        for c in S:
            ans.append(c * count[c])
            count[c] = 0
        for c in count:
            ans.append(c * count[c])
        return "".join(ans)


S = "cba"
T = "abcd"
test = Solution()
print(test.customSortString(S, T))
