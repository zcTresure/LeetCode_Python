# -*- coding: utf-8 -*-
# File:      剑指 Offer 22. 链表中倒数第k个节点.py
# DATA:      2021/9/2
# Software:  PyCharm
__author__ = 'zcFang'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 建立链表
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

    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        ans = head
        while k and head:
            head = head.next
            k -= 1
        while head:
            ans = ans.next
            head = head.next
        return ans


nums = [1, 2, 3, 4, 5]
k = 2
test = Solution()
head = test.build(nums)
print(test.getKthFromEnd(head, k).val)
