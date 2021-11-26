# File Name:  988. 从叶结点开始的最小字符串
# date:       2021/4/13
# encode:      UTF-8
__author__ = 'zcTresure'

from template import BinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
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
root = BinaryTree.build(nums)
print(test.smallestFromLeaf(root))
