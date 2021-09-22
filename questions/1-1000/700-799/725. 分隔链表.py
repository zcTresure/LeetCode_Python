# -*- coding: utf-8 -*-
# File:      725. 分隔链表.py
# DATA:      2021/9/22
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List
from template import LinkList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        n, temp = 0, head
        ans = [None] * k
        while temp:
            temp = temp.next
            n += 1
        quotient, remainder = n // k, n - (n // k) * k
        index = 0
        curr = head
        while curr and index < k:
            ans[index] = curr
            part_size = quotient + (0 if remainder > 0 else -1)
            remainder -= 1
            while part_size and curr.next:
                part_size -= 1
                curr = curr.next
            next = curr.next
            curr.next = None
            curr = next
            index += 1
        return ans


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
test = Solution()
head = LinkList.build(nums)
split = test.splitListToParts(head, 3)
