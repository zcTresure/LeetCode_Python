# File Name:  543. 二叉树的直径
# date:       2021/4/12
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

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.result = 1

        def heaper(node):
            if not node: return 0
            left_depth = heaper(node.left)
            right_depth = heaper(node.right)
            self.result = max(self.result, left_depth + right_depth + 1)
            return max(left_depth, right_depth) + 1

        heaper(root)
        return self.result - 1


nodes = [1, 2, 3, 4, 5]
test = Solution()
root = test.buildBinaryTree(nodes)
print(test.diameterOfBinaryTree(root))
