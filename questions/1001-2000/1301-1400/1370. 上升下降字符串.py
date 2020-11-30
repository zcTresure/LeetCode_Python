# File Name:  ${NAME}
# date:       ${DATE}
__author__ = "zcTresure"


class Solution:
    def sortString(self, s: str) -> str:
        num = [0] * 26
        for ch in s:
            num[ord(ch) - ord('a')] += 1
        ret = list()
        while len(ret) < len(s):
            for i in range(26):
                if num[i]:
                    ret.append(chr(i + ord('a')))
                    num[i] -= 1
            for i in range(25, -1, -1):
                if num[i]:
                    ret.append(chr(i + ord('a')))
                    num[i] -= 1
        return "".join(ret)


s = "aaaabbbbcccc"
test = Solution()
print(test.sortString(s))
