# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructTreeNodeDynamic(self, nums: list) -> TreeNode:
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

    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        left = right = None
        if root.left:
            left = root.left
        if root.right:
            right = root.right
        root.left = right
        root.right = left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root

    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root

    def preordPrint(self, root: TreeNode) -> None:
        if not root:
            return
        print(root.val, end=' ')
        self.preordPrint(root.left)
        self.preordPrint(root.right)


nums = [4, 2, 7, 1, 3, 6, 9]
test = Solution()
root = test.constructTreeNodeDynamic(nums)
root = test.invertTree(root)
test.preordPrint(root)
print()