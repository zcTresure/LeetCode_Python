import heapq


class Solution:
    # 堆排序
    def findKthLargest(self, nums: list, k: int) -> int:
        # 替换nums[i]后维护最小堆：自顶向下调整新元素位置，直至该值满足(parent value < son value)
        def shift(i, k):
            flag = 0
            while (i * 2 + 1) < k and flag == 0:
                t = i
                if nums[i] > nums[2 * i + 1]:
                    t = 2 * i + 1
                if (i * 2 + 2) < k and nums[t] > nums[2 * i + 2]:
                    t = 2 * i + 2
                if t == i:
                    flag = 1
                else:
                    nums[i], nums[t] = nums[t], nums[i]
                    i = t

        # O(k):建立大小为K的最小堆， k/2-1是最后一个非叶节点，因为shift是向下调整，所以倒序从最下面出发，不然(4 32 1)->(2 34 1)->(2 14 3)->(2 14 3) 结果不对
        for i in range(k // 2, -1, -1):
            shift(i, k)

        # O((N-k)logK)，剩余元素依次比较替换
        for i in range(k, len(nums)):
            if nums[0] < nums[i]:
                nums[0] = nums[i]
                shift(0, k)
        return nums[0]

    # 快速排序

    def __partition(self, nums, left, right):
        pivot = nums[left]
        j = left
        for i in range(left + 1, right + 1):
            if nums[i] < pivot:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[left], nums[j] = nums[j], nums[left]
        return j

    def findKthLargest(self, nums: list, k: int) -> int:
        size = len(nums)
        target = size - k
        left = 0
        right = size - 1
        while True:
            index = __partition(1, nums, left, right)
            if index == target:
                return nums[index]
            elif index < target:
                left = index + 1
            else:
                right = index - 1

    def findKthLargest(self, nums, k):
        # heapq中直接有这个函数
        return heapq.nlargest(k, nums)[-1]

    # 用堆，时间复杂度O(N + klog(N))
    def findKthLargest(self, nums, k):

        nums = [-num for num in nums]
        heapq.heapify(nums)
        res = float('inf')
        for _ in range(k):
            res = heapq.heappop(nums)
        return -res


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
test = Solution()
print(test.findKthLargest(nums, k))
