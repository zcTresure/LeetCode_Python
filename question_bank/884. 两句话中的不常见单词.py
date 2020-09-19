class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> list:
        count = {}
        for word in A.split():
            count[word] = count.get(word, 0) + 1
        for word in B.split():
            count[word] = count.get(word, 0) + 1
        return [word for word in count if count[word] == 1]


A = "apple apple"
B = "banana"
test = Solution()
print(test.uncommonFromSentences(A, B))
