from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        pre = 0
        n = len(arr)
        while pre < n:
            if arr[pre] == 0:
                arr.insert(pre + 1, 0)
                arr.pop()
                pre += 1
            pre += 1

    def duplicateZeros(self, arr: List[int]) -> None:
        top, n = 0, len(arr)
        i = -1
        while top < n:
            i += 1
            top += 1 if arr[i] else 2
        j = n - 1
        if top == n + 1:
            arr[j] = 0
            j -= 1
            i -= 1
        while j >= 0:
            arr[j] = arr[i]
            j -= 1
            if arr[i] == 0:
                arr[j] = arr[i]
                j -= 1
            i -= 1


arr = [1, 0, 2, 3, 0, 4, 5, 0]
Solution().duplicateZeros(arr)
print(arr)
