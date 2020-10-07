class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        # 直接使用heapq堆
        import heapq
        freq = {}
        res = []
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        # 1.我们需要按照数字出现频率进行排序，所以val在前，key在后
        # 2.我们需要最大堆，但是heapq只实现了最小堆，所以加个负号，模拟最大堆
        max_heap = [(-val, key) for key, val in freq.items()]
        heapq.heapify(max_heap)
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res


nums = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 6, 7]
k = 4
print(Solution().topKFrequent(nums, k))
