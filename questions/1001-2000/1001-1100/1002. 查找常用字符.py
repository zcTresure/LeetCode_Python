from collections import Counter


class Solution:
    def commonChars(self, A: list) -> list:
        mincount = [float("inf")] * 26
        for word in A:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            for i in range(26):
                mincount[i] = min(mincount[i], count[i])
        ans = []
        for i in range(26):
            ans.extend([chr(i + ord('a'))] * mincount[i])
        return ans


A = ["bella", "label", "roller"]
test = Solution()
print(test.commonChars(A))
