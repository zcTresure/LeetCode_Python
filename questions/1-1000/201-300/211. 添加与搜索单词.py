# File Name:  211. 添加与搜索单词
# date:       2021/3/27
# encode:      UTF-8
__author__ = 'zcTresure'

import collections


class WordDictionary:
    def __init__(self):
        self.d = {}  # 字典树

    def addWord(self, word: str) -> None:
        t = self.d  # 单词入字典树
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t['end'] = True  # 字典树叶子节点

    def search(self, word: str) -> bool:
        cut = False

        def dfs(td, s):  # 深搜 td:当前子字典树 s:当前字符串
            nonlocal cut  # 剪枝
            if cut:
                return True
            t = td
            for i, c in enumerate(s):
                if c == '.':  # 匹配通配符
                    return any(dfs(t[j], s[i + 1:]) for j in t if j != 'end')
                if c not in t:  # 没有找到该字符串
                    return False
                t = t[c]  # 进入子字典树中
            cut = 'end' in t  # 当前字典树是否有叶子节点
            return cut

        return dfs(self.d, word)


class WordDictionary:
    # 根据单词长度查找
    def __init__(self):
        self.d = collections.defaultdict(list)

    def addWord(self, word: str) -> None:
        self.d[len(word)] += [word]

    def search(self, word: str) -> bool:
        n = len(word)
        f = lambda s: all(map(lambda i: word[i] in {s[i], '.'}, range(n)))  # 匹配函数，比写正则要快不少
        return any(map(f, self.d[n]))

    def search(self, word: str) -> bool:  # 扩写版
        n = len(word)

        def f(s):
            for i in range(n):
                if word[i] not in {s[i], '.'}:
                    return False
            return True

        for s in self.d[n]:
            if f(s):
                return True
        return False


s = ["addWord", "addWord", "addWord", "search", "search", "search", "search"]
d = ["bad", "dad", "mad", "pad", "bad", ".ad", "b.."]
test = WordDictionary()
for i, word in enumerate(s):
    if word == "addWord":
        test.addWord(d[i])
    else:
        print(test.search(d[i]))
