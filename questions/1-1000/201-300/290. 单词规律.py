# Date:       2020/12/16
# Coding:      UTF-8
__author__ = "zcTresure"


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word2ch = dict()
        ch2word = dict()
        words = s.split()
        if len(pattern) != len(words):
            return False
        for ch, word in zip(pattern, words):
            if (word in word2ch and word2ch[word] != ch) or (ch in ch2word and ch2word[ch] != word):
                return False
            word2ch[word] = ch
            ch2word[ch] = word
        return True


pattern = "abba"
s = "dog cat cat dog"
test = Solution()
print(test.wordPattern(pattern, s))
