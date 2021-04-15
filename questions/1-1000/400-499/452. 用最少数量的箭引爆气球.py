

__author__ = "zcTresure"


class Solution:
    def findMinArrowShots(self, points: list) -> int:
        if not points:
            return 0
        points.sort(key=lambda balloon: balloon[1])
        pos = points[0][1]
        ans = 1
        for balloon in points:
            if balloon[0] > pos:
                pos = balloon[1]
                ans += 1
        return ans


points = [[10, 16], [2, 8], [1, 6], [7, 12]]
test = Solution()
print(test.findMinArrowShots(points))
