class Solution:
    # 暴力 超时
    def robot(self, command: str, obstacles: list, x: int, y: int) -> bool:
        curx, cury, index, n = 0, 0, 0, len(command)
        while True:
            if curx == x and cury == y:
                return True
            if [curx, cury] in obstacles or curx > x or cury > y:
                return False
            if command[index] == 'U':
                cury += 1
            else:
                curx += 1
            index = (index + 1) % n

    # 集合优化
    def robot(self, command: str, obstacles: list, x: int, y: int) -> bool:
        px ,py = 0,0
        path = set()  # set((0,0))是{0}，因此需要后面加上(0,0)才有效
        for s in command:
            if s == 'U':
                py += 1
            elif s == 'R':
                px += 1
            path.add((px, py))
        path.add((0, 0))
        p1 = x // px if px != 0 else 0
        p2 = y // py if py != 0 else 0
        p = min(p1, p2)
        for ob in obstacles:
            b1 = ob[0] // px if px != 0 else 0
            b2 = ob[1] // py if py != 0 else 0
            block = min(b1, b2)
            if ob[0] <= x and ob[1] <= y:  # 如果障碍的坐标大于终点坐标，则不用判断了
                r1 = ob[0] - block * px
                r2 = ob[1] - block * py
                if (r1, r2) in path:
                    return False
        res_x = x - p * px
        res_y = y - p * py
        if (res_x, res_y) in path:
            return True
        else:
            return False


command = "URR"
obstacles = [[4, 2]]
x, y = 3, 2
test = Solution()
print(test.robot(command, obstacles, x, y))
