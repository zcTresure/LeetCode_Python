class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(s in J for s in S)

    def numJewelsInStones(self, J: str, S: str) -> int:
        jewelsSet = set(J)
        return sum(s in jewelsSet for s in S)


J = "aA"
S = "aAAbbbb"
test = Solution()
print(test.numJewelsInStones(J, S))
