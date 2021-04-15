# File Name:  1315. 祖父节点值为偶数的节点和
# date:       2021/4/2
# encode:      UTF-8
__author__ = 'zcTresure'

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 二叉树的建立
    def buildBinaryTree(self, nums: list) -> TreeNode:
        if not nums: return TreeNode(-1)
        root = TreeNode(nums[0])
        Nodes, index = [root], 1
        for node in Nodes:
            if node != None:
                node.left = TreeNode(nums[index]) if nums[index] != None else None
                Nodes.append(node.left)
                index += 1
                if index == len(nums): return root
                node.right = TreeNode(nums[index]) if nums[index] != None else None
                Nodes.append(node.right)
                index += 1
                if index == len(nums):
                    return root

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(grandparent, parent, node):
            if not node: return
            if grandparent % 2 == 0:  # 祖父值为偶数，节点值加入答案
                self.ans += node.val
            dfs(parent, node.val, node.left)  # 递归调用左子树
            dfs(parent, node.val, node.right)  # 递归调用右子树

        dfs(1, 1, root)
        return self.ans

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        q = deque([root])
        ans = 0
        while len(q) > 0:
            node = q.popleft()
            if node.val % 2 == 0:  # 值为偶数
                if node.left:
                    if node.left.left:  # 孙子节点存在，则加入答案
                        ans += node.left.left.val
                    if node.left.right:
                        ans += node.left.right.val
                if node.right:
                    if node.right.left:
                        ans += node.right.left.val
                    if node.right.right:
                        ans += node.right.right.val
            if node.left:  # 孩子节点入队列
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return ans


nums = [6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5]
test = Solution()
root = test.buildBinaryTree(nums)
print(test.sumEvenGrandparent(root))
