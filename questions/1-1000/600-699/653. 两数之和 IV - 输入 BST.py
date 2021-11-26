# File Name:  653. 两数之和 IV - 输入 BST
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
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.flag = False
        vals = set()

        def heaper(node):
            if not node: return
            if node.val in vals:
                self.flag = True
                return
            else:
                vals.add(k - node.val)
            heaper(node.left)
            heaper(node.right)

        heaper(root)
        return self.flag


nums = [5, 7, 6, 2, 4, 7]
k = 14
test = Solution()
root = BinaryTree.build(nums)
print(test.findTarget(root, k))
