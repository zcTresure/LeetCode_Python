class Solution:
    def checkStraightLine(self, coordinates: list) -> bool:
        if len(coordinates) < 3:
            return True
        y = coordinates[1][1] - coordinates[0][1]
        x = coordinates[1][0] - coordinates[0][0]
        if x == 0:
            for i in range(2, len(coordinates)):
                xx = coordinates[i][0] - coordinates[i - 1][0]
                if x != xx:
                    return False
        else:
            k = y / x
            for i in range(2, len(coordinates)):
                yy = coordinates[i][1] - coordinates[i - 1][1]
                xx = coordinates[i][0] - coordinates[i - 1][0]
                if xx == 0:
                    return False
                if yy / xx != k:
                    return False
        return True


coordinates = [[1, 1], [2, 2], [2, 0]]
test = Solution()
print(test.checkStraightLine(coordinates))
