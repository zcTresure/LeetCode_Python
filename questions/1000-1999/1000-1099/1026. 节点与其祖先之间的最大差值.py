# File Name:  1026. 节点与其祖先之间的最大差值
# date:       2021/4/14
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

    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.result = -1

        def dfs(node, max_val, min_val):
            if not node:
                self.result = max(self.result, max_val - min_val)
            else:
                max_val, min_val = max(max_val, node.val), min(min_val, node.val)
                dfs(node.left, max_val, min_val)
                dfs(node.right, max_val, min_val)

        dfs(root, 0, 100001)
        return self.result


nums = [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]
test = Solution()
root = test.buildBinaryTree(nums)
print(test.maxAncestorDiff(root))
