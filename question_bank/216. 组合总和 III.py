class Solution:
    # 回溯
    def combinationSum3(self, k: int, n: int) -> list:
        ans = list()

        def backtrack(tmp: list, index: int, k: int, n: int):
            if len(tmp) == k and n == sum(tmp):
                ans.append(tmp[:])
                return
            for i in range(index, min(n, 10)):
                tmp.append(i)
                backtrack(tmp, i + 1, k, n)
                tmp.pop()
        backtrack([], 1, k, n)
        return ans

    # 二进制（子集）枚举
    def combinationSum3(self, k: int, n: int) -> list:
        ans = list()
        tmp = list()

        def check(mask: int, k: int, n: int) -> bool:
            for i in range(9):
                if i << 1 and mask:
                    tmp.append(i + 1)
            return len(tmp) == k and sum(tmp) == n
        for mask in range(1 << 9):
            # tmp.clear()
            if check(mask, k, n):
                ans.append(tmp[:])
        return ans


n, k = 9, 3
print(Solution().combinationSum3(k, n))
print(1 << 9)
