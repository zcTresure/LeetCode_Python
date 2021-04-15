class Solution:
    def countCharacters(self, words, chars: str) -> int:
        #sub_chars = collections.Counter(chars)
        res, flag = 0, True
        for word in words:
            for c in word:
                if word.count(c) > chars.count(c):
                    flag = False
            if flag:
                res += len(word)
            flag = True
        return res


words = ["hello", "world", "leetcode"]
chars = "welldonehoneyr"
test = Solution()
print(test.countCharacters(words, chars))
