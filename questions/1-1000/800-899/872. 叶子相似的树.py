# # File Name:  872. 叶子相似的树
# # date:       2021/3/24
# # encode:      UTF-8
# __author__ = 'zcTresure'

from template import BinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def preOrder(root: TreeNode):
            if root:
                if not root.left and not root.right:
                    yield root.val
                yield from preOrder(root.left)
                yield from preOrder(root.right)

        return list(preOrder(root1)) == list(preOrder(root2))


nums1 = [1]
nums2 = [2]
test = Solution()
root1 = BinaryTree.build(nums1)
root2 = BinaryTree.build(nums2)
print(test.leafSimilar(root1, root2))
