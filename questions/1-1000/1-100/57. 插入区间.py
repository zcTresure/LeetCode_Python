# File Name:  ${NAME}
# date:       ${DATE}
__author__ = "zcTresure"


class Solution:
    def insert(self, intervals: list, newInterval: list) -> list:
        left, right = newInterval
        placed = False
        ans = list()
        for l, r in intervals:
            if right < l:
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append([l, r])
            elif r < left:
                ans.append([l, r])
            else:
                left = min(left, l)
                right = max(right, r)
        if not placed:
            ans.append([left, right])
        return ans


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
test = Solution()
print(test.insert(intervals, newInterval))
