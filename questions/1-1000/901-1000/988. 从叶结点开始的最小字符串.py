# File Name:  988. 从叶结点开始的最小字符串
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

    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.result = "~"

        def dfs(node, chars):
            if node:
                chars.append(chr(node.val + ord('a')))
                if not (node.left or node.right):
                    self.result = min(self.result, "".join(reversed(chars)))
                dfs(node.left, chars)
                dfs(node.right, chars)
                chars.pop()

        dfs(root, [])
        return self.result


nums = [0, 1, 2, 3, 4, 3, 4]
test = Solution()
root = test.buildBinaryTree(nums)
print(test.smallestFromLeaf(root))
