# Date:       2020/12/20
# Coding:      UTF-8
__author__ = "zcTresure"


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counts = [0] * 26
        visited = [0] * 26
        strs = list()
        for c in s:
            counts[ord(c) - ord('a')] += 1
        for c in s:
            if not visited[ord(c) - 97]:
                while strs and strs[-1] > c:
                    if counts[ord(strs[-1]) - 97] > 0:
                        visited[ord(strs[-1]) - 97] = 0
                        strs.pop()
                    else:
                        break
                visited[ord(c) - 97] = 1
                strs.append(c)
            counts[ord(c) - 97] -= 1
            print(strs)

        return ''.join(strs)


s = "cbacdcbc"
test = Solution()
print(test.removeDuplicateLetters(s))
