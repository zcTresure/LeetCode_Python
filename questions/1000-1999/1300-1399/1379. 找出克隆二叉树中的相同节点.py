# File Name:  1379. 找出克隆二叉树中的相同节点
# date:       2021/4/15
# encode:      UTF-8
__author__ = 'zcTresure'


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildBinaryTree(self, nums: list) -> TreeNode:
        if not nums: return None
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

    def findNode(self, root: TreeNode, target: int) -> TreeNode:
        self.target_node = None

        def dfs(node):
            if node:
                if node.val == target:
                    self.target_node = node
                    return
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return self.target_node

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack1, stack2 = [original], [cloned]
        while stack1:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if node1 == target:
                return node2
            if node1.right:
                stack1.append(node1.right)
                stack2.append(node2.right)
            if node1.left:
                stack1.append(node1.left)
                stack2.append(node2.left)


nums = [7, 4, 3, None, None, 6, 19]
target = 3
test = Solution()
root = test.buildBinaryTree(nums)
target_node = test.findNode(root, target)
clone = test.buildBinaryTree(nums)
result = test.getTargetCopy(root, clone, target_node)
