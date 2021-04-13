# File Name:  面试题 17.12. BiNode
# date:       2021/4/13
# encode:      UTF-8
__author__ = 'zcTresure'


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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

    def preOrder(self, root: TreeNode) -> None:
        if not root:
            print('None', end=' ')
            return
        print(root.val, end=' ')
        self.preOrder(root.left)
        self.preOrder(root.right)

    def convertBiNode(self, root: TreeNode) -> TreeNode:
        self.ans = self.pre = None

        def inorder(node):
            if not node: return None
            inorder(node.left)
            node.left = None
            if self.pre: self.pre.right = node
            if not self.pre: self.ans = node
            self.pre = node
            inorder(node.right)

        inorder(root)
        return self.ans


nums = [4, 2, 5, 1, 3, None, 6, 0]
test = Solution()
root = test.buildBinaryTree(nums)
test.preOrder(root)
print()
root = test.convertBiNode(root)
test.preOrder(root)
