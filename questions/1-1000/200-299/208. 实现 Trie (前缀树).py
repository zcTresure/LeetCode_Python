# File Name:  208. 实现 Trie (前缀树)
# date:       2021/4/14
# encode:      UTF-8
__author__ = 'zcTresure'


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = [None] * 26
        self.is_end = False

    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for char in prefix:
            ch = ord(char) - ord('a')
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for char in word:
            ch = ord(char) - ord('a')
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.searchPrefix(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.searchPrefix(prefix) is not None

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
