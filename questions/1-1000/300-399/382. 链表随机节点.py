# -*- coding: utf-8 -*-
# File:    382. 链表随机节点.py
# Date:    2022/1/16
# Software: Pycharm
__author__ = 'zcFang'

from random import choice
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.arr = []
        while head:
            self.arr.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return choice(self.arr)

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
