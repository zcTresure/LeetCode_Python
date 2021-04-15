# File Name:  1006. 笨阶乘
# date:       2021/4/1
# encode:      UTF-8
__author__ = 'zcTresure'


class Solution:
    def clumsy(self, N: int) -> int:
        stack = [N]
        caclucate = 0
        N -= 1
        while N > 0:
            if caclucate % 4 == 0:
                stack.append(stack.pop() * N)
            elif caclucate % 4 == 1:
                stack.append(int(stack.pop() / N))
            elif caclucate % 4 == 2:
                stack.append(N)
            else:
                stack.append(-N)
            N -= 1
            caclucate += 1
        return sum(stack)


N = 10
test = Solution()
print(test.clumsy(N))
