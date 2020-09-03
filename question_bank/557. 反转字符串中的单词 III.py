class Solution:
    # 用栈保存每个单词
    def reverseWords(self, s: str) -> str:
        stack = []
        s += ' '
        ss = ''
        for c in s:
            if c != ' ':
                stack.append(c)
            else:
                while stack:
                    ss += stack.pop()
                ss += c
        return ss[:-1]

    # 字符串分割
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        res = ""
        for item in s:
            res += "".join(item[::-1]) + " "
        return res[:-1]

    def reverseWords(self, s: str) -> str:
        return " ".join(item[::-1]for item in s.split(' '))

    def reverseWords(self, s: str) -> str:
        s = s[::-1]
        print(s)
        s = s.split(' ')
        s = s[::-1]
        return ' '.join(s)


s = "Let's take LeetCode contest"
test = Solution()
print(test.reverseWords(s))
