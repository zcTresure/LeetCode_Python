class Solution:
    # 数学 + 缩小问题规模
    def getPermutation(self, n: int, k: int) -> str:
        factorials = [1]
        # 计算每个数的阶乘
        for i in range(1, n):
            factorials.append(i * factorials[-1])
        k -= 1
        ans = list()
        valid = [1] * (n + 1)
        for i in range(1, n + 1):
            order = k // factorials[n - i] + 1
            for j in range(1, n + 1):
                order -= valid[j]
                if order == 0:
                    ans.append(str(j))
                    valid[j] = 0
                    break
            k %= factorials[n - i]
        return "".join(ans)

    # 回溯 + 剪枝
    def getPermutation(self, n: int, k: int) -> str:
        if n == 0:
            return ""
        used = [False] * (n + 1)
        path = []
        factorial = [1] * (n + 1)
        for i in range(2, n + 1):
            factorial[i] = factorial[i - 1] * i

        def dfs(n: int, k: int, index: int):
            if index == n:
                return
            cnt = factorial[n - 1 - index]
            for i in range(1, n + 1):
                if used[i]:
                    continue
                if cnt < k:
                    k -= cnt
                    continue
                path.append(str(i))
                used[i] = True
                dfs(n, k, index + 1)
                return
        dfs(n, k, 0)
        return ''.join(path)


while 1:
    n = int(input("input:"))
    k = int(input("input:"))
    test = Solution()
    print(test.getPermutation(n, k))
