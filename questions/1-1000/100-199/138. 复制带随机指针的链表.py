# -*- coding: utf-8 -*-
# File:    138. 复制带随机指针的链表.py
# Date:    2021/7/22
# Software: Pycharm
__author__ = 'zcFang'


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # 建立链表
    def build(self, nums: list) -> Node:
        if not nums:
            return Node(-1)
        head = Node(nums[0])
        pre = head
        for i in range(1, len(nums)):
            cur = Node(nums[i])
            pre.next = cur
            pre = pre.next
        return head

    # 打印链表
    def Print(self, head: Node) -> None:
        while head:
            print(head.val, end='')
            head = head.next
            if head:
                print(' ', end='')
            else:
                print()

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        h1 = head
        while h1:  # 新建节点间隔插入链表 如[1 2 3 4 5] -> [1 1 2 2 3 3 4 4 5 5]
            node = Node(h1.val)
            node.next = h1.next
            h1.next = node
            h1 = node.next
        h1 = head
        while h1:  # 将新节点的随机节点部署
            now_node = h1.next
            now_node.random = h1.random.next if h1.random else None
            h1 = h1.next.next
        now_head, h1 = head.next, head
        while h1:  # 分割原始链表和新链表
            now_node = h1.next
            h1.next = h1.next.next
            now_node.next = h1.next.next if h1.next else None
            h1 = h1.next
        return now_head


nums = [7, 13, 11, 10, 1]
test = Solution()
head = test.build(nums)
head1 = test.copyRandomList(head)
test.Print(head1)
