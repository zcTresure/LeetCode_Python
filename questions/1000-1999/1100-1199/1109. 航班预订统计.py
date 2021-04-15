class Solution:
    def corpFlightBookings(self, bookings: list, n: int) -> list:
        counters = [0] * n
        for booking in bookings:
            counters[booking[0] - 1] += booking[2]
            if booking[1] < n:
                counters[booking[1]] -= booking[2]
        for i in range(1, n):
            counters[i] += counters[i - 1]
        return counters


bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
n = 5
test = Solution()
print(test.corpFlightBookings(bookings, n))
