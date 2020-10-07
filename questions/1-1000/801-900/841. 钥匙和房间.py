import collections


class Solution:
    def canVisitAllRooms(self, rooms: list) -> bool:
        vis = set()
        n = len(rooms)
        num = 0

        def dfs(x: int):
            vis.add(x)
            nonlocal num
            num += 1
            for room in rooms[x]:
                if room not in vis:
                    dfs(room)
        dfs(0)
        return num == n

    def canVisitAllRooms(self, rooms: list) -> bool:
        vis = set()
        vis.add(0)
        n = len(rooms)
        num = 0
        que = collections.deque([0])

        while que:
            x = que.popleft()
            num += 1
            for room in rooms[x]:
                if room not in vis:
                    vis.add(room)
                    que.append(room)
        return num == n


rooms = [[1, 3], [3, 0, 1], [2], [0]]
test = Solution()
print(test.canVisitAllRooms(rooms))
