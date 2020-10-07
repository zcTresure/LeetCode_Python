class Solution:
    def getValidT9Words(self, num: str, words: list) -> list:
        res = []
        key = ['2', '2', '2', '3', '3', '3', '4', '4', '4', '5', '5', '5',  # 构造字母与数字对应数组
               '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '9', '9', '9', '9']
        for word in words:
            # index为num索引 flag判断单词是否在数组
            index, flag = 0, True
            for c in word:                                                  # 逐个对应单词中的字母
                # ord(c) - ord('a')得到每个字母到'a'的距离
                if num[index] == key[ord(c) - ord('a')]:
                    index += 1                                              # 字母匹配成功 继续匹配下个字母
                else:
                    flag = False                                            # 匹配失败 直接跳过
                    break
            if flag:
                # 匹配成功 将word加入数组中
                res.append(word)
        return res


num = "8733"
words = ["tree", "used"]
test = Solution()
print(test.getValidT9Words(num, words))
