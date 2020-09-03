def duplicateZeros(self, arr: list) -> None:
    pre = 0
    n = len(arr)
    while pre < n:
        if arr[pre] == 0:
            arr.insert(pre + 1, 0)
            arr.pop()
            pre += 1
        pre += 1


arr = [8, 4, 5, 0, 0, 0, 0, 7]
duplicateZeros(1, arr)
print(arr)
