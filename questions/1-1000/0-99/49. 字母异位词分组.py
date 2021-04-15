# Date:       2020/12/14
# encode:      UTF-8
__author__ = "zcTresure"

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for st in strs:
            key = ''.join(sorted(st))
            mp[key].append(st)
        return list(mp.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord('a')] += 1
            mp[tuple(counts)].append(st)
        return list(mp.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
test = Solution()
print(test.groupAnagrams(strs))
