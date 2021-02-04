# Date:       2021/1/31
# Coding:      UTF-8
__author__ = "zcTresure"


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        f = list(range(n))

        def find(x: int) -> int:
            if f[x] == x:
                return x
            f[x] = find(f[x])
            return f[x]

        def check(a: str, b: str) -> bool:
            num = 0
            for ac, bc in zip(a, b):
                if ac != bc:
                    num += 1
                    if num > 2:
                        return False
            return True

        for i in range(n):
            for j in range(i + 1, n):
                fi, fj = find(i), find(j)
                if fi == fj:
                    continue
                if check(strs[i], strs[j]):
                    f[fi] = fj

        ret = sum(1 for i in range(n) if f[i] == i)
        return ret
