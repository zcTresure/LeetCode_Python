# File Name:  ${NAME}
# date:       ${DATE}
__author__ = "zcTresure"

from collections import defaultdict


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        Choices = defaultdict()
        for k in key:
            if k in Choices:
                continue
            else:
                Choices[k] = []
                for ri, r in enumerate(ring):
                    if r == k:
                        Choices[k].append(ri)
        counter = [{0: 0}]
        Path = defaultdict()
        for keyi in range(len(key)):
            counter.append({})
            for choice in Choices[key[keyi]]:
                temp = []
                for start in counter[keyi].keys():
                    previous_distance = counter[keyi][start]
                    s = str(start) + "-" + str(choice)
                    if s not in Path:
                        d1 = abs(choice - start)
                        d2 = abs(len(ring) - d1)
                        newc = min(d1, d2)
                        Path[s] = newc
                    temp.append(previous_distance + Path[s])
                counter[keyi + 1][choice] = min(temp) + 1
        final = min(counter[-1].values())
        return final

    def findRotateSteps(self, ring: str, key: str) -> int:
        n, m = len(ring), len(key)
        pos = [[] for _ in range(26)]
        for i in range(n):
            pos[ord(ring[i]) - ord('a')].append(i)
        dp = [[float("inf")] * n for _ in range(m)]
        for i in pos[ord(key[0]) - ord('a')]:
            dp[0][i] = min(i, n - i) + 1
        for i in range(m):
            for j in pos[ord(key[i]) - ord('a')]:
                for k in pos[ord(key[i - 1]) - ord('a')]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + min(abs(j - k), n - abs(j - k)) + 1)
        return min([dp[m - 1][i] for i in range(n)])


ring = "godding"
key = "gd"
test = Solution()
print(test.findRotateSteps(ring, key))
