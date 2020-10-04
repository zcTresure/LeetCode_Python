from collections import Counter
class Solution:
    def avoidFlood(self, rains: list) -> list:
        n = len(rains)
        ans = [0] * n
        