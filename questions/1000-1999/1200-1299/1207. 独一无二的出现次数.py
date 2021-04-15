from collections import defaultdict


class Solution:
    def uniqueOccurrences(self, arr: list) -> bool:
        count = defaultdict(int)
        for i in range(len(arr)):
            count[arr[i]] += 1
        tmp = set()
        print(count)
        for c in count.values():
            if c in tmp:
                return False
            else:
                tmp.add(c)
        return True

arr = [1,2,2,1,3]
test = Solution()
print(test.uniqueOccurrences(arr))