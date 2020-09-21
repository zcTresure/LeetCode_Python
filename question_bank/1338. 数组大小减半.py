import collections


class Solution:
    def minSetSize(self, arr: list) -> int:
        counts = collections.Counter(arr)
        cnt, ans = 0, 0
        for num, count in counts.most_common():
            cnt += count
            ans += 1
            if cnt * 2 >= len(arr):
                return ans
        return -1


arr = [9, 77, 63, 22, 92, 9, 14, 54, 8, 38, 18, 19, 38, 68, 58, 19]
test = Solution()
print(test.minSetSize(arr))
