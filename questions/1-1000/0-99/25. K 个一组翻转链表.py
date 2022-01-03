# -*- coding: utf-8 -*-
# File:      25. K 个一组翻转链表.py
# DATA:      2022/1/3
# Software:  PyCharm
__author__ = 'zcFang'

from typing import Optional

# Definition for singly-linked list.
import LinkList


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 翻转一个子链表，并且返回头部和尾部
    def reverse(self, head: ListNode, tail: ListNode) -> tuple:
        prev, p = tail.next, head
        while prev != tail:
            next = p.next
            p.next = prev
            prev = p
            p = next
        return tail, head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        while head:
            tail = prev
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            next = tail.next
            head, tail = self.reverse(head, tail)
            prev.next, tail.next = head, next
            prev, head = tail, tail.next
        return dummy.next


head = [1, 2, 3, 4, 5]
k = 2
head = LinkList.build(head)
LinkList.Print(head)
head = Solution().reverseKGroup(head, k)
LinkList.Print(head)
