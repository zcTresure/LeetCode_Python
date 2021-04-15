# File Name:  1603. 设计停车系统
# date:       2021/3/19
# oding:      UTF-8
__author__ = 'zcTresure'


class ParkingSystem:

    # def __init__(self, big: int, medium: int, small: int):
    #     self.big = big
    #     self.medium = medium
    #     self.small = small
    #
    # def addCar(self, carType: int) -> bool:
    #     if carType == 1 and self.big > 0:
    #         self.big -= 1
    #         return True
    #     elif carType == 2 and self.medium > 0:
    #         self.medium -= 1
    #         return True
    #     elif carType == 3 and self.small > 0:
    #         self.small -= 1
    #         return True
    #     return False

    def __init__(self, big: int, medium: int, small: int):
        self.num_car = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self.num_car[carType] > 0:
            self.num_car[carType] -= 1
            return True
        return False


t = ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
count = [[1, 1, 0], [1], [2], [3], [1]]
test = ParkingSystem(1, 1, 0)
for i in range(1, len(count)):
    print(test.addCar(count[i][0]))

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
