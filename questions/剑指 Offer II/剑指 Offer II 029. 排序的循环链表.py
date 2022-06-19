# -*- coding: utf-8 -*-
# File:      剑指 Offer II 029. 排序的循环链表.py
# DATA:      2022/6/18
# Software:  PyCharm


# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def build(self, nums: List[int]) -> 'Node':
        if not nums:
            return Node()
        head = Node(nums[0])
        head.next = head
        pre = head
        for i in range(1, len(nums)):
            cur = Node(nums[i])
            cur.next = pre.next
            pre.next = cur
            pre = pre.next
        return head

    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        node = Node(insertVal)
        if head is None:
            node.next = node
            return node
        if head.next == head:
            head.next = node
            node.next = head
            return head
        curr = head
        next = head.next
        while next != head:
            if curr.val <= insertVal <= next.val:
                break
            if curr.val > next.val:
                if insertVal > curr.val or insertVal < next.val:
                    break
            curr = curr.next
            next = next.next
        curr.next = node
        node.next = next
        return head


def Print(head: 'Node') -> None:
    pre = head
    while head:
        print(head.val, end=' ')
        head = head.next
        if head == pre:
            break
    print()


nums = [3, 4, 1]
insertVal = 2
head = Solution().build(nums)
Print(head)
Solution().insert(head, insertVal)
