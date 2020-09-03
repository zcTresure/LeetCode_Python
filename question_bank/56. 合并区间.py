class Solution:
    def merge(self, intervals: list) -> list:
        intervals.sort(key=lambda x: x[0])
        merged = list()
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1]=max(merged[-1][1],interval[1])
        return merged


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
test = Solution()
print(test.merge(intervals))
