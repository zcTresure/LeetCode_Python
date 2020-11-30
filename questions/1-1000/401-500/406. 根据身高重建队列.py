# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "zcTresure"


class Solution:
    def reconstructQueue(self, people: list) -> list:
        people.sort(key=lambda x: (-x[0], x[1]))
        n = len(people)
        ans = list()
        for person in people:
            ans.insert(person[1], person)
        return ans

    def reconstructQueue(self, people: list) -> list:
        people.sort(key=lambda x: (x[0], (-x[1])))
        n = len(people)
        ans = [[] for _ in range(n)]
        for person in people:
            position = person[1] + 1
            for i in range(n):
                if not ans[i]:
                    position -= 1
                    if position == 0:
                        ans[i] = person
                        break
        return ans


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
test = Solution()
print(test.reconstructQueue(people))
