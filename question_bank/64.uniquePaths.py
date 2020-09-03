def uniquePaths(self, m: int, n: int) -> int:
    cur = [1] * m
    for i in range(1, n):
        for j in range(1, m):
            cur[j] = cur[j - 1] + cur[j]
    return cur[-1]

print(uniquePaths(1,7,3))