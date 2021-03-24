

__author__ = "zcTresure"


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructBTree(self, nums: list) -> TreeNode:
        if nums[0] == None:
            return None
        root = TreeNode(nums[0])
        Nodes, index = [root], 1
        for node in Nodes:
            if node != None:
                node.left = TreeNode(
                    nums[index]) if nums[index] != None else None
                Nodes.append(node.left)
                index += 1
                if index == len(nums):
                    return root
                node.right = TreeNode(
                    nums[index]) if nums[index] != None else None
                Nodes.append(node.right)
                index += 1
                if index == len(nums):
                    return root

    def countNodes(self, root: TreeNode) -> int:
        def exists(root: TreeNode, level: int, k: int):
            bits = 1 << (level - 1)
            while root and bits > 0:
                if bits & k == 0:
                    root = root.left
                else:
                    root = root.right
                bits >>= 1
            return root != None

        if not root:
            return 0
        level = 0
        node = root
        while node.left:
            level += 1
            node = node.left
        low = 1 << level
        high = (1 << (level + 1)) - 1
        while low < high:
            mid = (high - low + 1) // 2 + low
            if exists(root, level, mid):
                low = mid
            else:
                high = mid - 1
        return low

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
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
test = Solution()
root = test.constructBTree(nums)
print(test.countNodes(root))
