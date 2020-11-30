# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "zcTresure"


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def build(self, nums: list) -> ListNode:
        if not nums:
            return
        head = ListNode(nums[0])
        pre = head
        for i in range(1, len(nums)):
            cur = ListNode(nums[i])
            pre.next = cur
            pre = pre.next
        return head

    # 打印链表
    def Print(self, head: ListNode) -> None:
        while head:
            print(head.val, end='')
            head = head.next
            if head:
                print(' ', end='')
            else:
                print()

    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur, insert = head, head.next
        while insert:
            if cur.val > insert.val:
                cur.next = insert.next
                pre, last = dummy, dummy.next
                while last and insert.val > last.val:
                    pre = pre.next
                    last = last.next
                insert.next = last
                pre.next = insert
                insert = cur.next
            else:
                cur = cur.next
                insert = insert.next
        return dummy.next

    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        last, insert = head, head.next
        while insert:
            if last.val >= insert.val:
                pre = dummy
                while pre.next.val < insert.val:
                    pre = pre.next
                last.next = insert.next
                insert.next = pre.next
                pre.next = insert
            else:
                last = last.next
            insert = last.next
        return dummy.next


nums = [4, 1, 3, 2]
test = Solution()
link = test.build(nums)
link = test.insertionSortList(link)
test.Print(link)
