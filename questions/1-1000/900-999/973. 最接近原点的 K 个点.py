

__author__ = "zcTresure"

import heapq
import random


class Solution:
    def kClosest(self, points: list, K: int) -> list:
        points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:K]

    def kClosest(self, points: list, K: int) -> list:
        def random_select(left: int, right: int, K: int):
            pivot_id = random.randint(left, right)
            pivot = points[pivot_id][0] ** 2 + points[pivot_id][1] ** 2
            points[right], points[pivot_id] = points[pivot_id], points[right]
            i = left - 1
            for j in range(left, right):
                if points[j][0] ** 2 + points[j][1] ** 2 <= pivot:
                    i += 1
                    points[i], points[j] = points[j], points[i]
            i += 1
            points[i], points[right] = points[right], points[i]
            if K < i - left + 1:
                random_select(left, i - 1, K)
            elif K > i - left + 1:
                random_select(i + 1, right, K - (i - left + 1))

        n = len(points)
        random_select(0, n - 1, K)
        return points[:K]

    def kClosest(self, points: list, K: int) -> list:
        q = [(-x ** 2 - y ** 2, i) for i, (x, y) in enumerate(points[:K])]
        heapq.heapify(q)
        for i in range(K, len(points)):
            dist = -points[i][0] ** 2 - points[i][1] ** 2
            heapq.heappushpop(q, (dist, i))
        ans = [points[index] for _, index in q]
        return ans


points = [[1, 3], [-2, 2]]
K = 1
test = Solution()
print(test.kClosest(points, K))
