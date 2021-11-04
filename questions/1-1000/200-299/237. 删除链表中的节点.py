# -*- coding: utf-8 -*-
# File:      237. 删除链表中的节点.py
# DATA:      2021/11/2
# Software:  PyCharm
__author__ = 'zcFang'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node: ListNode) -> None:
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

