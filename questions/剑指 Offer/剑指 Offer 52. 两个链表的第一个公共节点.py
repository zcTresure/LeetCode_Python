# -*- coding: utf-8 -*-
# File:    剑指 Offer 52. 两个链表的第一个公共节点.py
# Date:    2021/7/21
# Software: Pycharm
__author__ = 'zcFang'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        m, n, d = 0, 0, 0
        h_a, h_b = headA, headB
        while h_a:
            h_a = h_a.next
            m += 1
        while h_b:
            h_b = h_b.next
            n += 1
        if n < m:
            d = m - n
            h_a, h_b = headA, headB
        else:
            d = n - m
            h_b, h_a = headA, headB
        while d:
            h_a = h_a.next
            d -= 1
        while h_a != h_b:
            h_a = h_a.next
            h_b = h_b.next
        return h_a


nums1 = [4, 1, 8, 4, 5]
nums2 = [5, 0, 1, 8, 4, 5]
test = Solution()
head1 = test.build(nums1)
head2 = test.build(nums2)
test.Print(head1)
test.Print(head2)
node = test.getIntersectionNode(head1, head2)
print(node)
