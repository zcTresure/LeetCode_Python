# Definition for a binary tree node.
import BinaryTree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def getPath(root: TreeNode, target: TreeNode) -> list:
            path = list()
            node = root
            while node != target:
                path.append(node)
                if target.val > node.val:
                    node = node.right
                else:
                    node = node.left
            path.append(node)
            return path

        p_path = getPath(root, p)
        q_path = getPath(root, q)
        ancestor = None
        for x, y in zip(p_path, q_path):
            if x == y:
                ancestor = x
            else:
                break
        return ancestor

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestor = root
        while True:
            if p.val < ancestor.val and q.val < ancestor.val:
                ancestor = ancestor.left
            elif p.val > ancestor.val and q.val > ancestor.val:
                ancestor = ancestor.right
            else:
                break
        return ancestor


nums = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
p, q = 2, 8
root = BinaryTree.build(nums)
node_p = BinaryTree.findNode(root, p)
node_q = BinaryTree.findNode(root, q)
print(Solution().lowestCommonAncestor(root, node_p, node_q).val)
