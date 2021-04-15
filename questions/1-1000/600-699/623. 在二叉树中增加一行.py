# File Name:  623. 在二叉树中增加一行
# date:       2021/4/11
# encode:      UTF-8
__author__ = 'zcTresure'

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 二叉树的建立
    def buildBinaryTree(self, nums: list) -> TreeNode:
        if not nums:
            return TreeNode(-1)
        root = TreeNode(nums[0])
        nodes, index, n = [root], 1, len(nums)
        for node in nodes:
            if node != None:
                if index == n:
                    return root
                node.left = TreeNode(nums[index]) if nums[index] != None else None
                nodes.append(node.left)
                index += 1
                if index == n:
                    return root
                node.right = TreeNode(nums[index]) if nums[index] != None else None
                nodes.append(node.right)
                index += 1

    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:  # 第一层添加节点特殊处理
            node = TreeNode(val)
            node.left = root
            return node
        queue = deque([root])
        level = 1
        while queue:
            level += 1  # 从第二层开始
            if level == depth:
                n = len(queue)
                for _ in range(n):
                    node = queue.popleft()
                    left_node, right_node = TreeNode(val), TreeNode(val)
                    left_node.left, right_node.right = node.left, node.right  # 左子树接左孩子，右子树接右孩子
                    node.left, node.right = left_node, right_node  # 添加一层节点
            n = len(queue)  # 每一层节点数
            tmp = []  # 记录每一层节点值
            for _ in range(n):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root

    def levelOrder(self, root: TreeNode) -> None:
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                print(node.val, end='')
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if q:
                    print(end=' ')
        print()


nodes = [4, 2, None, 3, 1]
test = Solution()
root = test.buildBinaryTree(nodes)
test.levelOrder(root)
val, depth = 1, 3
root = test.addOneRow(root, val, depth)
test.levelOrder(root)
