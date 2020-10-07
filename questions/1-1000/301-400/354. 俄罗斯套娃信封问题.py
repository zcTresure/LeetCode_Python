from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, envelopes: list) -> int:
        def lis(nums: list) -> int:
            dp = list()
            for i in range(len(nums)):
                idx = bisect_left(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
                print(dp)
            return len(dp)

        envelopes.sort(key=lambda x: (x[0], -x[1]))
        return lis([nums[1] for nums in envelopes])


envelopes = [[1, 2], [2, 3], [3, 4], [3, 5],
             [4, 5], [5, 5], [5, 6], [6, 7], [7, 8]]
test = Solution()
print(test.maxEnvelopes(envelopes))

dp = [4, 1, 0]
print(bisect_left(dp, 3))
