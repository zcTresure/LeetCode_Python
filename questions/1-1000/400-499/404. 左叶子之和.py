import collections


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

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def lnode(node): return not node.left and not node.right

        def dfs(node: TreeNode) -> int:
            ans = 0
            if node.left:
                ans += node.left.val if lnode(node.left) else dfs(node.left)
            if node.right and not lnode(node.right):
                ans += dfs(node.right)
            return ans
        return dfs(root) if root else 0

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

nums = [3, 9, 20, None, None, 15, 7]
test = Solution()
root = test.constructTreeNodeDynamic(nums)
print(test.sumOfLeftLeaves(root))
