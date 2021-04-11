# File Name:  236. 二叉树的最近公共祖先
# date:       2021/4/11
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

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = root

        def dfs(root, p, q):
            if not root: return False
            left_son = dfs(root.left, p, q)
            right_son = dfs(root.right, p, q)
            if (left_son and right_son) or ((root.val == p.val or root.val == q.val) and (left_son or right_son)):
                self.ans = root
            return left_son or right_son or (root.val == q.val or root.val == p.val)

        dfs(root, p, q)
        return self.ans


nodes = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
p = 5
q = 1
test = Solution()
root = test.buildBinaryTree(nodes)
print(test.lowestCommonAncestor(root))
