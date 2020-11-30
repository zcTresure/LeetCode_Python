# File Name:  ${NAME}
# date:       ${DATE}
__author__ = "zcTresure"


class Solution:
    def canCompleteCircuit(self, gas: list, cost: list) -> int:
        n, i = len(gas), 0
        while i < n:
            sGas = sCost = cnt = 0
            while cnt < n:
                j = (i + cnt) % n
                sGas += gas[j]
                sCost += cost[j]
                if sGas < sCost:
                    break
                cnt += 1
            if cnt == n:
                return i
            else:
                i += cnt + 1
            print(i)
        return -1

    def canCompleteCircuit(self, gas: list, cost: list) -> int:
        spare = minSpare = start = 0
        for i in range(len(gas)):
            spare += gas[i] - cost[i]
            if spare < minSpare:
                minSpare = spare
                start = i + 1
        return -1 if spare < 0 else start

    def canCompleteCircuit(self, gas: list, cost: list) -> int:
        n = len(gas)
        spare, minSpare, start = 0, float("inf"), 0
        for i in range(n):
            spare += gas[i] - cost[i]
            if spare < minSpare:
                minSpare = spare
                start = i
        return -1 if spare < 0 else (start + 1) % n


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
test = Solution()
print(test.canCompleteCircuit(gas, cost))
