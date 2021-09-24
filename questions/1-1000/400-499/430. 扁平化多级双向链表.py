# -*- coding: utf-8 -*-
# File:      430. 扁平化多级双向链表.py
# DATA:      2021/9/24
# Software:  PyCharm
__author__ = 'zcFang'


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def dfs(head: 'Node') -> 'Node':
            prev, curr = None, head

            while curr:
                next = curr.next

                # 如果有子节点，那么首先处理子节点
                if curr.child:
                    child = dfs(curr.child)
                    next = curr.next

                    #  将当前节点与 child 相连
                    curr.next = curr.child
                    curr.next.prev = curr

                    # 如果 next 不为空，就将最后孩子节点与 next 相连
                    if next:
                        child.next = next
                        next.prev = child

                    # 将 child 置为空
                    curr.child = None
                    prev = child
                else:
                    prev = curr
                curr = next

            return prev

        dfs(head)
        return head
