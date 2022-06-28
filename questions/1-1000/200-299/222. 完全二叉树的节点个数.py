import BinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def exists(self, root: TreeNode, level: int, k: int):
        bits = 1 << (level - 1)
        while root and bits > 0:
            if bits & k == 0:
                root = root.left
            else:
                root = root.right
            bits >>= 1
        return root != None

    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        level = 0  # 树的层数
        node = root
        while node.left:  # 计算树的层数
            level += 1
            node = node.left
        low = 1 << level  # 树中节点个数最少为 2**level 个
        high = (1 << (level + 1)) - 1  # 树中节点个数最多个数
        while low < high:
            mid = (high - low + 1) // 2 + low
            if self.exists(root, level, mid):
                low = mid
            else:
                high = mid - 1
        return low

    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        ans = 0

        def preOrder(root: TreeNode):
            nonlocal ans
            if root:
                ans += 1
            if root.left:
                preOrder(root.left)
            if root.right:
                preOrder(root.right)

        preOrder(root)
        return ans



nums = [1, 2, 3, 4, 5, 6]
root = BinaryTree.build(nums)
print(Solution().countNodes(root))
