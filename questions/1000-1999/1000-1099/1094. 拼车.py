from typing import List
import heapq


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # 按上车的地点升序
        trips.sort(key=lambda x: x[1])
        off_dist = []
        for i in range(len(trips)):
            dist = trips[i][1]
            while off_dist and dist >= off_dist[0][0]:
                _, passenger = heapq.heappop(off_dist)
                # 空座位 + 下车乘客
                capacity += passenger
            # 空座位数减去要该地点上车的人数
            capacity -= trips[i][0]
            # 座位不够直接返回
            if capacity < 0:
                return False
            heapq.heappush(off_dist, [trips[i][2], trips[i][0]])
        return True

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        car = []
        for count, enter, exit in trips:
            # 上车的地点和人数
            car.append([enter, count])
            # 下车的地点和人数
            car.append([exit, -count])
        # 按照地点进行升序序
        car.sort()
        for _, count in car:
            # 空座位减去该地点上车的人数
            capacity -= count
            # 座位不够直接返回
            if capacity < 0:
                return False

        return True


# trips = [[2, 1, 5], [3, 3, 7]]
# capacity = 4
trips = [[2, 1, 5], [3, 3, 7]]
capacity = 5
test = Solution()
print(test.carPooling(trips, capacity))
