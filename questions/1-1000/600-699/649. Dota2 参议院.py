# Date:       2020/12/11
# encode:      UTF-8
__author__ = "zcTresure"

from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()
        for i in range(n):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            if radiant[0] > dire[0]:
                dire.append(n + dire[0])
            else:
                radiant.append(n + radiant[0])
            dire.popleft()
            radiant.popleft()
        return "Radiant" if radiant else "Dire"


senate = "RDD"
test = Solution()
print(test.predictPartyVictory(senate))
