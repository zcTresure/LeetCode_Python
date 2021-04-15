from collections import Counter


class Solution:
    def commonChars(self, A: list) -> list:
        minCount = [float("inf")] * 26
        for word in A:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            for i in range(26):
                minCount[i] = min(minCount[i], count[i])
        ans = []
        for i in range(26):
            ans.extend([chr(i + ord('a'))] * minCount[i])
        return ans


A = ["bella", "label", "roller"]
test = Solution()
print(test.commonChars(A))
