

__author__ = "zcTresure"

from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list) -> int:
        def addWord(word: str):
            if word not in wordId:
                nonlocal nodeNum
                wordId[word] = nodeNum
                nodeNum += 1

        def addEdge(word: str):
            addWord(word)
            id1 = wordId[word]
            chars = list(word)
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = "*"
                newWord = "".join(chars)
                addWord(newWord)
                id2 = wordId[newWord]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = tmp

        wordId = dict()
        edge = defaultdict(list)
        nodeNum = 0
        for word in wordList:
            addEdge(word)
        addEdge(beginWord)
        if endWord not in wordId:
            return 0
        disBegin = [float("inf")] * nodeNum
        beginId = wordId[beginWord]
        disBegin[beginId] = 0
        queBegin = deque([beginId])
        disEnd = [float("inf")] * nodeNum
        endId = wordId[endWord]
        disEnd[endId] = 0
        queEnd = deque([endId])
        while queBegin or queEnd:
            queBeginSize = len(queBegin)
            for _ in range(queBeginSize):
                nodeBegin = queBegin.popleft()
                if disEnd[nodeBegin] != float("inf"):
                    return (disBegin[nodeBegin] + disEnd[nodeBegin]) // 2 + 1
                for it in edge[nodeBegin]:
                    if disBegin[it] == float("inf"):
                        disBegin[it] = disBegin[nodeBegin] + 1
                        queBegin.append(it)
            queEndSize = len(queEnd)
            for _ in range(queEndSize):
                nodeEnd = queEnd.popleft()
                if disBegin[nodeEnd] != float("inf"):
                    return (disBegin[nodeEnd] + disEnd[nodeEnd]) // 2 + 1
                for it in edge[nodeEnd]:
                    if disEnd[it] == float("inf"):
                        disEnd[it] = disEnd[nodeEnd] + 1
                        queEnd.append(it)
        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
test = Solution()
print(test.ladderLength(beginWord, endWord, wordList))
