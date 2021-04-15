# File Name:  101. 对称二叉树
# date:       2021/4/11
# encode:      UTF-8
__author__ = 'zcTresure'


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

    def isSymmetric(self, root: TreeNode) -> bool:
        def heaper(lefts, rights):
            if not lefts and not rights: return True
            if not lefts or not rights:
                return False
            if lefts.val != rights.val or (not lefts and rights) or (lefts and not rights):
                return False
            return heaper(lefts.left, rights.right) and heaper(lefts.right, rights.left)

        return heaper(root.left, root.right)


nodes = [1, 2, 2, 3, 4, 4,3]
test = Solution()
root = test.buildBinaryTree(nodes)
print(test.isSymmetric(root))
