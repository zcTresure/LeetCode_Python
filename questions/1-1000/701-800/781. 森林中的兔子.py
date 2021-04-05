# File Name:  781. 森林中的兔子
# date:       2021/4/5
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List
from collections import Counter


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        print(count.keys(), count.values())
        ans = sum((x + y) // (y + 1) * (y + 1) for y, x in count.items())
        return ans


answers = [1, 1, 2, 2]
test = Solution()
print(test.numRabbits(answers))
