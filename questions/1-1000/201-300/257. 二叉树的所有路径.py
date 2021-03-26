from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructTreeNodeDynamic(self, nums: list) -> TreeNode:
        if nums[0] == None:
            return TreeNode(-1)
        root = TreeNode(nums[0])
        Nodes, index = [root], 1
        for node in Nodes:
            if node != None:
                node.left = TreeNode(nums[index]) if nums[index] != None else None
                Nodes.append(node.left)
                index += 1
                if index == len(nums):
                    return root
                node.right = TreeNode(nums[index]) if nums[index] != None else None
                Nodes.append(node.right)
                index += 1
                if index == len(nums):
                    return root

    # 深度优先搜索
    def binaryTreePaths(self, root: TreeNode) -> list:
        paths = list()

        def allPaths(root: TreeNode, path: str):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += '->'
                    allPaths(root.left, path)
                    allPaths(root.right, path)
        allPaths(root, '')
        return paths

    # 广度优先搜索
    def binaryTreePaths(self, root: TreeNode) -> list:
        paths = list()
        if not root:
            return paths
        node_queue = deque([root])
        path_queue = deque([str(root.val)])
        while node_queue:
            node = node_queue.popleft()
            path = path_queue.popleft()
            if not node.left and not node.right:
                paths.append(path)
            else:
                if node.left:
                    node_queue.append(node.left)
                    path_queue.append(path + '->' + str(node.left.val))
                if node.right:
                    node_queue.append(node.right)
                    path_queue.append(path + '->' + str(node.right.val))
        return paths


nums = [1, 2, 3, None, 5]
test = Solution()
root = test.constructTreeNodeDynamic(nums)
print(test.binaryTreePaths(root))
