# File Name:  剑指 Offer 68 - II. 二叉树的最近公共祖先
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

    # 查找节点
    def findNode(self, root: TreeNode, target: int) -> TreeNode:
        self.target_node = None

        def dfs(node):
            if node:
                if node.val == target:
                    self.target_node = node
                    return
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return self.target_node

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.result = None

        def heaper(node, p, q):
            if not node: return False
            left_son = heaper(node.left, p, q)
            right_son = heaper(node.right, p, q)
            if (left_son and right_son) or ((node.val == p.val or node.val == q.val) and (left_son or right_son)):
                self.result = node
            return left_son or right_son or (node.val == p.val or node.val == q.val)

        heaper(root, p, q)
        return self.result


nodes = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
p = 5
q = 1
test = Solution()
root = test.buildBinaryTree(nodes)
node_p = test.findNode(root, p)
node_q = test.findNode(root, q)
print(test.lowestCommonAncestor(root, node_p, node_q).val)
