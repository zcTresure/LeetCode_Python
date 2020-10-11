from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, S: str, words: list) -> int:
        def subseq(word: str):
            it = iter(S)
            return all(x in it for x in word)

        return sum(subseq(word) for word in words)

    def numMatchingSubseq(self, S: str, words: list) -> int:
        waiting = defaultdict(list)
        for word in words:
            # 存储以w[0]开头的前缀，此时waiting = {'a': [[], ['c', 'd'], ['c', 'e']], 'b': [['b']]}
            waiting[word[0]].append(iter(word[1:]))
        for c in S:
            for it in waiting.pop(c, ()):
                # 在本题的例子中 it 分别为[]、['c', 'd']、['c', 'e']
                waiting[next(it, None)].append(it)
        return len(waiting[None])


S = "abcde"
words = ["a", "bb", "acd", "ace"]
test = Solution()
print(test.numMatchingSubseq(S, words))
