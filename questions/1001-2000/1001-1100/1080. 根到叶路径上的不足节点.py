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

    # 当前结点是否被删除
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def dfs(node: TreeNode, sumVal: int) -> bool:
            if not node.left and not node.right:
                return (sumVal + node.val) < limit
            lDel, rDel = True, True
            if node.left:
                lDel = dfs(node.left, sumVal + node.val)
            if node.right:
                rDel = dfs(node.right, sumVal + node.val)
            if lDel:
                node.left = None
            if rDel:
                node.right = None
            return lDel and rDel
        if dfs(root, 0):
            return None
        return root

    # 当前结点是否被保留
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def dfs(node: TreeNode, sumVal: int) -> bool:
            if not node.left and not node.right:
                return (node.val + sumVal) >= limit
            lDel, rDel = False, False
            if node.left:
                lDel = dfs(node.left, sumVal + node.val)
            if node.right:
                rDel = dfs(node.right, sumVal + node.val)
            if not lDel:
                node.left = None
            if not rDel:
                node.right = None
            return lDel or rDel
        if not dfs(root, 0):
            return None
        return root


nums = [1, 2, 3, 4, -99, -99, 7, 8, 9, -99, -99, 12, 13, -99, 14]
limit = 1
test = Solution()
root = test.constructBTree(nums)
root = test.sufficientSubset(root, limit)
if root:
    test.levelorderPrint(root)
