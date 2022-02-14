from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> list:
        count = {}
        for word in A.split():
            count[word] = count.get(word, 0) + 1
        for word in B.split():
            count[word] = count.get(word, 0) + 1
        return [word for word in count if count[word] == 1]

    # 哈希表
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        freq = Counter(s1.split()) + Counter(s2.split())

        ans = list()
        for word, occ in freq.items():
            if occ == 1:
                ans.append(word)

        return ans


A = "apple apple"
B = "banana"
test = Solution()
print(test.uncommonFromSentences(A, B))
