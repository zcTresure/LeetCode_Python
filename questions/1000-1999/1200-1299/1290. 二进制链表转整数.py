# -*- coding: utf-8 -*-
# File:      1290. 二进制链表转整数.py
# DATA:      2022/6/16
# Software:  PyCharm

from template import LinkList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head:
            ans = ans * 2 + head.val
            head = head.next
        return ans


nums = [1, 0, 1]
head = LinkList.build(nums)
print(Solution().getDecimalValue(head))
