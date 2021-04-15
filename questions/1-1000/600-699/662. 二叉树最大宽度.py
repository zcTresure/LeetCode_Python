# File Name:  662. 二叉树最大宽度
# date:       2021/4/12
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

    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        queue = [(root, 0, 0)]
        cur_depth = left = ans = 0
        for node, depth, pos in queue:
            if node:
                queue.append((node.left, depth + 1, pos * 2))  # 左孩子到当前层最左边的节点个数
                queue.append((node.right, depth + 1, pos * 2 + 1))  # 右孩子到当前层最左边节点的个数
                if cur_depth != depth:
                    cur_depth = depth
                    left = pos
                ans = max(ans, pos - left + 1)  # 当前层的宽度
        return ans



nums = [1, 3, 2, 5, 3, None, 9]
test = Solution()
root = test.buildBinaryTree(nums)
print(test.widthOfBinaryTree(root))
