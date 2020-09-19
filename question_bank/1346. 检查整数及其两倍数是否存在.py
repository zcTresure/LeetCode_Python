import collections

class Solution:
    # 暴力
    def checkIfExist(self, arr: list) -> bool:
        for i, a in enumerate(arr):
            for j, b in enumerate(arr):
                if i != j and a * 2 == b:
                    return True
        return False

    # 双指针
    def checkIfExist(self, arr: list) -> bool:
        arr.sort()
        q = 0
        for p in range(len(arr)):
            while q < len(arr) and arr[p] * 2 > arr[q]:
                q += 1
            if q != len(arr) and p != q and arr[p] * 2 == arr[q]:
                return True
        q = len(arr) - 1
        for p in range(len(arr) - 1, -1, -1):
            while q > -1 and arr[p] * 2 < arr[q]:
                q -= 1
            if q != -1 and p != q and arr[p] * 2 == arr[q]:
                return True
        return False

    # 哈希表
    def checkIfExist(self, arr: list) -> bool:
        counter = collections.Counter(arr)
        for n in arr:
            if n != 0 and counter[2 * n] >= 1:
                return True
            if n == 0 and counter[2 * n] >= 2:
                return True
        return False


arr = [7, 1, 14, 11]
test = Solution()
print(test.checkIfExist(arr))
