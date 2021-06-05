# -*- coding: utf-8 -*-
# File:     203. 移除链表元素.py
# Date:     2021/6/5
# Software: PyCharm
__author__ = 'zcFang'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def build(self, nums: list) -> ListNode:
        if not nums:
            return ListNode(-1)
        head = ListNode(nums[0])
        pre = head
        for i in range(1, len(nums)):
            cur = ListNode(nums[i])
            pre.next = cur
            pre = pre.next
        return head

    def Print(self, head: ListNode) -> None:
        while head:
            print(head.val, end='')
            head = head.next
            if head:
                print(' ', end='')
            else:
                print()

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre, cur = dummy, head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        return dummy.next


nums = [1, 2, 6, 3, 4, 5, 6, 6]
val = 6
test = Solution()
head = test.build(nums)
head = test.removeElements(head, val)
test.Print(head)
