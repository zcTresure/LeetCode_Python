# Date:       2020/12/20
# encode:      UTF-8
__author__ = "zcTresure"


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counts = [0] * 26
        visited = [0] * 26
        strs = list()
        for c in s:
            counts[ord(c) - ord('a')] += 1
        for c in s:
            # 当前字符没有访问过，进行处理判断
            if not visited[ord(c) - 97]:
                # 当栈不空且栈顶字符小于当前字符判断是否要出栈
                while strs and strs[-1] > c:
                    # 当前字符个数不为零时，说明后面还有相同的字符，则弹出栈顶，并重新标记
                    if counts[ord(strs[-1]) - 97] > 0:
                        visited[ord(strs[-1]) - 97] = 0
                        strs.pop()
                    else:
                        break
                # 标记当前字符已访问
                visited[ord(c) - 97] = 1
                strs.append(c)
            counts[ord(c) - 97] -= 1

        return ''.join(strs)


s = "cbacdcbc"
test = Solution()
print(test.removeDuplicateLetters(s))
