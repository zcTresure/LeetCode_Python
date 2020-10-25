class Solution:
    def getWinner(self, arr: list, k: int) -> int:
        res, count = -1, 0
        tmp = arr[0]
        for i in range(1, len(arr)):
            if tmp > arr[i]:
                count += 1
            else:
                tmp = arr[i]
                count = 1
            if count == k:
                return tmp
        return tmp


arr = [1,11,22,33,44,55,66,77,88,99]
k = 1000000000
test = Solution()
print(test.getWinner(arr, k))
