# File Name:  面试题 04.03. 特定深度节点链表
# date:       2021/3/28
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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

    # 打印链表
    def Print(self, head: ListNode) -> None:
        while head:
            print(head.val, end='')
            head = head.next
            if head:
                print(' ', end='')
            else:
                print()

    # 二叉树的建立
    def buildBinaryTree(self, nums: list) -> TreeNode:
        if not nums:
            return TreeNode(-1)
        root = TreeNode(nums[0])
        Nodes, index = [root], 1
        for node in Nodes:
            if node != None:
                node.left = TreeNode(nums[index]) if nums[index] != None else None
                Nodes.append(node.left)
                index += 1
                if index == len(nums):
                    return root
                node.right = TreeNode(nums[index]) if nums[index] != None else None
                Nodes.append(node.right)
                index += 1
                if index == len(nums):
                    return root

    # 特定深度节点链表
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        ans = []
        queue = deque()
        queue.append(tree)
        while queue:
            n = len(queue)
            tmp = list()
            for i in range(n):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                if i == 0:
                    head = ListNode(node.val)
                    cur = head
                else:
                    cur.next = ListNode(node.val)
                    cur = cur.next
            ans.append(head)
        return ans


nums = [1, 2, 3, 4, 5, None, 7, 8]
test = Solution()
root = test.buildBinaryTree(nums)
ans = test.listOfDepth(root)
for i in range(len(ans)):
    test.Print(ans[i])