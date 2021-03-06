# Date:       2021/2/10
# Coding:      UTF-8
__author__ = "zcTresure"

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 统计 s1 中每个字符出现的次数
        counter1 = Counter(s1)
        N = len(s2)
        # 定义滑动窗口的范围是 [left, right]，闭区间，长度与s1相等
        left = 0
        right = len(s1) - 1
        # 统计窗口s2[left, right - 1]内的元素出现的次数
        counter2 = Counter(s2[0:right])
        while right < N:
            # 把 right 位置的元素放到 counter2 中
            counter2[s2[right]] += 1
            # 如果滑动窗口内各个元素出现的次数跟 s1 的元素出现次数完全一致，返回 True
            if counter1 == counter2:
                return True
            # 窗口向右移动前，把当前 left 位置的元素出现次数 - 1
            counter2[s2[left]] -= 1
            # 如果当前 left 位置的元素出现次数为 0， 需要从字典中删除，否则这个出现次数为 0 的元素会影响两 counter 之间的比较
            if counter2[s2[left]] == 0:
                del counter2[s2[left]]
            # 窗口向右移动
            left += 1
            right += 1
        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False
        count1 = [0] * 26
        count2 = [0] * 26
        for i in range(m):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        if count1 == count2:
            return True
        for i in range(m, n):
            count2[ord(s2[i]) - ord('a')] += 1
            count2[ord(s2[i - m]) - ord('a')] -= 1
            if count1 == count2:
                return True
        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        count = [0] * 26
        for i in range(m):
            count[ord(s1[i]) - ord('a')] -= 1
            count[ord(s2[i]) - ord('a')] += 1
        diff = 0
        for c in count:
            diff += 1 if c != 0 else 0
        if diff == 0:
            return True
        for i in range(m, n):
            x = ord(s2[i]) - ord('a')
            y = ord(s1[i % m]) - ord('a')
            print(x, y, diff)
            print(count)
            if x == y:
                continue
            # count[x] += 1
            # count[y] -= 1
            # if count[x] == 0:
            #     diff -= 1
            # else:
            #     diff += 1
            # if count[y] == 0:
            #     diff += 1
            # else:
            #     diff -= 1
            if count[x] == 0:
                diff += 1
            count[x] += 1
            if count[x] == 0:
                diff -= 1
            if count[y] == 0:
                diff += 1
            count[y] -= 1
            if count[y] == 0:
                diff -= 1

            if diff == 0:
                return True
        return False


test = Solution()
s1 = "ab"
s2 = "bba"
# s2 = "eidabooo"
print(test.checkInclusion(s1, s2))
