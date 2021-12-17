# -*- coding: utf-8 -*-
# File:      206. 反转链表.py
# DATA:      2021/12/17
# Software:  PyCharm
__author__ = 'zcFang'

from template import LinkList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    link = LinkList.build(nums)
    link = Solution().reverseList(link)
    LinkList.Print(link)
