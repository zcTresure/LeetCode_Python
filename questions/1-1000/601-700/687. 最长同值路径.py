# File Name:  687. 最长同值路径
# date:       2021/4/13
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

    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.result = 0

        def heaper(node):
            if not node: return 0
            left_length = heaper(node.left)
            right_length = heaper(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            self.result = max(self.result, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        heaper(root)
        return self.result


nums = [5, 5, 5, 1, 1, 5]
test = Solution()
root = test.buildBinaryTree(nums)
print(test.longestUnivaluePath(root))
