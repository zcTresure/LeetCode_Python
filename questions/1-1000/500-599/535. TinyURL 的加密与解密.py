# -*- coding: utf-8 -*-
# File:      535. TinyURL 的加密与解密.py
# DATA:      2022/6/29
# Software:  PyCharm

# 自增
from random import randrange


class Codec:
    def __init__(self):
        self.database = {}
        self.id = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.id += 1
        self.database[self.id] = longUrl
        return "https://tinyurl.com" + str(self.id)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        i = shortUrl.rfind('/')
        id = int(shortUrl[i + 1:])
        return self.database[id]


# 哈希生成
class Codec:

    def __init__(self):
        self.K1 = 1117
        self.K2 = 10 ** 9 + 7
        self.database = {}
        self.urlToKey = {}

    def encode(self, longUrl: str) -> str:
        if longUrl in self.urlToKey:
            return "http://tinyurl.com/" + str(self.urlToKey[longUrl])
        key, base = 0, 1
        for c in longUrl:
            key = (key + ord(c) * base) % self.K2
            base = (base * self.K1) % self.K2
        while key in self.database:
            key = (key + 1) % self.K2
        self.database[key] = longUrl
        self.urlToKey[longUrl] = key
        return "http://tinyurl.com/" + str(key)

    def decode(self, shortUrl: str) -> str:
        i = shortUrl.rfind('/')
        key = int(shortUrl[i + 1:])
        return self.database[key]


# 随机生成
class Codec:
    def __init__(self):
        self.dataBase = {}

    def encode(self, longUrl: str) -> str:
        while True:
            key = randrange(maxsize)
            if key not in self.dataBase:
                self.dataBase[key] = longUrl
                return "http://tinyurl.com/" + str(key)

    def decode(self, shortUrl: str) -> str:
        i = shortUrl.rfind('/')
        key = int(shortUrl[i + 1:])
        return self.dataBase[key]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
