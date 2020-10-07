class Solution:
    def floodFill(self, image: list, sr: int, sc: int, newColor: int) -> list:
        m, n = len(image), len(image[0])
        color = image[sr][sc]

        def dfs(x: int, y: int) -> None:
            if image[x][y] == color:
                image[x][y] = newColor
                for newX, newY in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= newX < m and 0 <= newY < n and image[newX][newY] == color:
                        dfs(newX, newY)
        if color != newColor:
            dfs(sr, sc)
        return image


image = [[0,0,0],[0,0,0]]
sr, sc, newColor = 1, 1, 0
test = Solution()
image = test.floodFill(image, sr, sc, newColor)
for i in range(len(image)):
    print(image[i])