# 小白解法
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        lastCh, isAdd = "x", 1
        res = ""
        while isAdd:
            isAdd = 0
            if a >= b >= c or a >= c >= b:
                if lastCh != "a":
                    if a >= 2:
                        res += "aa"; a -= 2
                    elif a == 1:
                        res += "a"; a -= 1
                    lastCh = "a"; isAdd = 1
                else:
                    if b >= c and b >= 1:
                        res += "b"; lastCh = "b"; b -= 1; isAdd = 1
                    elif c >= b and c >= 1:
                        res += "c"; lastCh = "c"; c -= 1; isAdd = 1
            elif b >= a >= c or b >= c >= a:
                if lastCh != "b":
                    if b >= 2:
                        res += "bb"; b -= 2
                    elif b == 1:
                        res += "b"; b -= 1
                    lastCh = "b"; isAdd = 1
                else:
                    if a >= c and a >= 1:
                        res += "a"; lastCh = "a"; a -= 1; isAdd = 1
                    elif c >= a and c >= 1:
                        res += "c"; lastCh = "c"; c -= 1; isAdd = 1
            elif c >= a >= b or c >= b >= a:
                if lastCh != "c":
                    if c >= 2:
                        res += "cc"; c -= 2
                    elif c == 1:
                        res += "c"; c -= 1
                    lastCh = "c"; isAdd = 1
                else:
                    if a >= b and a >= 1:
                        res += "a"; lastCh = "a"; a -= 1; isAdd = 1
                    elif b >= a and b >= 1:
                        res += "b"; lastCh = "b"; b -= 1; isAdd = 1
        return res

    # 贪心算法，加入最多的字符。如果会构成三个连续，则加入次多的算符。
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        m = {'a': a, 'b': b, 'c': c}
        res = ''
        while True:
            # 将字典数组按照字符个数进行排序
            temp = sorted([(k, v) for k, v in m.items()],
                          key = lambda x: x[1], reverse = True)
            if len(res) >= 2 and res[-1] == res[-2] and res[-1] == temp[0][0]:
                if m[temp[1][0]] == 0:# 当次多的字符为0 则没有字符可以添加 直接结束
                    break             # 否则则添加第二多的字符
                res += temp[1][0]
                m[temp[1][0]] -= 1
            else:
                if m[temp[0][0]] == 0:
                    break
                res += temp[0][0]
                m[temp[0][0]] -= 1
        return res


a, b, c = 1, 1, 7
test = Solution()
print(test.longestDiverseString(a, b, c))
