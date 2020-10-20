class Solution:
    def countGoodTriplets(self, arr: list, a: int, b: int, c: int) -> int:
        n = len(arr)
        ans = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if -a <= arr[i] - arr[j] <= a and -b <= arr[j] - arr[k] <= b and -c <= arr[i] - arr[k] <= c:
                        ans += 1
        return ans

    # 取 abs(arr[i]-arr[j])<=a 和 (arr[i]-arr[k])<=b 两个区间的交集
    def countGoodTriplets(self, arr: list, a: int, b: int, c: int) -> int:
        ans = 0
        n = len(arr)
        total = [0] * 1001
        for j in range(n):
            for k in range(j + 1, n):
                if -b <= arr[j] - arr[k] <= b:
                    lj, rj = arr[j] - a, arr[j] + a
                    lk, rk = arr[k] - c, arr[k] + c
                    # 交集的左顶点
                    l = max(0, lj, lk)
                    # 交集的右顶点
                    r = min(1000, rj, rk)
                    # 如果交集不为空
                    if l <= r:
                        ans += total[r] if l == 0 else total[r] - total[l - 1]
            for k in range(arr[j], 1001):
                total[k] += 1
        return ans


arr = [3, 0, 1, 1, 9, 7]
a = 7
b = 2
c = 3
test = Solution()
print(test.countGoodTriplets(arr, a, b, c))
