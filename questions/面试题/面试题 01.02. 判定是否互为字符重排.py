from collections import defaultdict, Counter


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        set1 = defaultdict()
        set2 = defaultdict()
        for i in range(len(s1)):
            if s1[i] not in set1:
                set1[s1[i]] = 0
            else:
                set1[s1[i]] += 1
            if s2[i] not in set2:
                set2[s2[i]] = 0
            else:
                set2[s2[i]] += 1
        return set1 == set2

    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return Counter(s1) == Counter(s2)


s1 = "abc"
s2 = "bca"
test = Solution()
print(test.CheckPermutation(s1, s2))
