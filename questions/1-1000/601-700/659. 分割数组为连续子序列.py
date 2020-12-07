# Date:       2020/12/4
# Coding:      UTF-8
__author__ = "zcTresure"

import collections, heapq


class Solution:
    def isPossible(self, nums: list) -> bool:
        mp = collections.defaultdict(list)
        for x in nums:
            if queue := mp.get(x - 1):
                prevLength = heapq.heappop(queue)
                heapq.heappush(mp[x], prevLength + 1)
            else:
                heapq.heappush(mp[x], 1)

        return not any(queue and queue[0] < 3 for queue in mp.values())

    def isPossible(self, nums: list) -> bool:
        countMap = collections.Counter(nums)
        endMap = collections.Counter()

        for x in nums:
            if countMap[x] > 0:
                prevEndCount = endMap.get(x - 1, 0)
                if prevEndCount > 0:
                    countMap[x] -= 1
                    endMap[x - 1] = prevEndCount - 1
                    endMap[x] += 1
                else:
                    if countMap.get(x + 1, 0) > 0 and countMap.get(x + 2, 0) > 0:
                        countMap[x] -= 1
                        countMap[x + 1] -= 1
                        countMap[x + 2] -= 1
                        endMap[x + 2] += 1
                    else:
                        return False
        return True


nums = [1, 2, 3, 3, 4, 5]
test = Solution()
print(test.isPossible(nums))
