class Solution:
    def duplicateZeros(self, arr: list) -> None:
        pre = 0
        n = len(arr)
        while pre < n:
            if arr[pre] == 0:
                arr.insert(pre + 1, 0)
                arr.pop()
                pre += 1
            pre += 1


arr = [1, 0, 2, 3, 0, 4, 5, 0]
Solution().duplicateZeros(arr)
print(arr)
