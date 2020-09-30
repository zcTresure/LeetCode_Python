import collections


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

    # 递归
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        def dfs(node: TreeNode):
            if not node:
                return
            if node.val > val:
                if node.left:
                    dfs(node.left)
                else:
                    node.left = TreeNode(val)
                    return
            else:
                if node.right:
                    dfs(node.right)
                else:
                    node.right = TreeNode(val)
                    return
        dfs(root)
        return root

    # 迭代
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        node = root
        while node:
            if node.val > val:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    break
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    break
        return root

    # 层次遍历
    def levelorderPrint(self, root: TreeNode) -> None:
        q = collections.deque()
        q.append(root)
        while q:
            node = q.popleft()
            print(node.val, end='')
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if q:
                print(end=' ')
        print()


nums = [4, 2, 7, 1, 3]
val = 5
test = Solution()
root = test.constructBTree(nums)
root = test.insertIntoBST(root, val)
test.levelorderPrint(root)
