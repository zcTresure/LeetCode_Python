class Solution:
    # 暴力 时间超限
    def maxProfitAssignment(self, difficulty: list, profit: list, worker: list) -> int:
        m, n = len(profit), len(worker)
        salary = [0] * n
        for i in range(m):
            for j in range(n):
                if difficulty[i] <= worker[j] and profit[i] > salary[j]:
                    salary[j] = profit[i]
        return sum(salary)

    # 排序
    def maxProfitAssignment(self, difficulty: list, profit: list, worker: list) -> int:
        jobs = list(zip(difficulty, profit))
        jobs.sort()
        ans, i, best, n = 0, 0, 0, len(jobs)
        for skill in sorted(worker):
            while i < n and skill >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i += 1
            ans += best
        return ans


difficulty = [2, 4, 6, 8, 10]
profit = [10, 20, 30, 40, 50]
worker = [4, 5, 6, 7]
test = Solution()
print(test.maxProfitAssignment(difficulty, profit, worker))
