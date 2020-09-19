class Solution:
    def canPlaceFlowers(self, flowerbed: list, n: int) -> bool:
        if n == 0:
            return True
        cnt = 0
        m = len(flowerbed)
        flowerbed.insert(m, 0)
        flowerbed.insert(0, 0)
        for i in range(1, m + 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                cnt += 1
        return cnt >= n


flowerbed = [1, 0, 0, 0, 1]
n = 1
test = Solution()
print(test.canPlaceFlowers(flowerbed, 1))
