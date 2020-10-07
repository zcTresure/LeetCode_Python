import heapq


class Solution:
    # N指针，N为列表个数
    def smallestRange(self, nums: list) -> list:
        n = len(nums)
        if n == 0:
            return [nums[0][0], nums[0][0]]
        index_l = [0] * n
        elem_l = [0] * n
        for i in range(n):
            elem_l[i] = nums[i][index_l[i]]
        minnum, maxnum = min(elem_l), max(elem_l)
        while True:
            curminnum, curmaxnum = min(elem_l), max(elem_l)
            if curmaxnum - curminnum < maxnum - minnum:
                maxnum, minnum = curmaxnum, curminnum
            index = elem_l.index(curminnum)
            if index_l[index] < len(nums[index]) - 1:
                index_l[index] += 1
                elem_l[index] = nums[index][index_l[index]]
            else:
                break
        return [min(elem_l), max(elem_l)]

    # N指针 + 最小堆，N为列表个数
    def smallestRange(self, nums: list) -> list:
        k = len(nums)
        elem_id_index = [(elem[0], id, 0) for id, elem in enumerate(nums)]
        heapq.heapify(elem_id_index)
        maxnum, minnum = 1e5, -1e5
        currmaxnum = max(elem_id_index)[0]

        # recursion
        while True:
            currminnum, id, index = heapq.heappop(elem_id_index)
            if currmaxnum - currminnum < maxnum - minnum:
                maxnum = currmaxnum
                minnum = currminnum
            if index < len(nums[id]) - 1:
                num = nums[id][index + 1]
                currmaxnum = max(currmaxnum, num)
                heapq.heappush(elem_id_index, (num, id, index + 1))
            else:
                break
        return [minnum, maxnum]


nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
test = Solution()
print(test.smallestRange(nums))
