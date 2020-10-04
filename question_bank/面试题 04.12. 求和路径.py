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
                node.right = TreeNode( nums[index]) if nums[index] != None else None
                Nodes.append(node.right)
                index += 1
                if index == len(nums):
                    return root

    def pathSum(self, root: TreeNode, target: int) -> int:
        if not root:
            return 0
        return self.path(root, target) + self.pathSum(root.left, target) + self.pathSum(root.right, target)

    def path(self, root: TreeNode, target: int) -> int:
        if not root:
            return 0
        res = 0
        if root.val == target:
            res += 1
        res += self.path(root.left, target - root.val)
        res += self.path(root.right, target - root.val)
        return res

    def pathSum(self, root: TreeNode, target: int) -> int:
        def helper(node: TreeNode, path: list):
            if node:
                path = [i + node.val for i in path] + [node.val]
                return path.count(target) + helper(node.left, path) + helper(node.right, path)
            return 0

        return helper(root, [])

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


target = 22
nums = [5,4,8,11,None,13,4,7,2,None,None,5,1]
test = Solution()
root = test.constructBTree(nums)
print(test.pathSum(root, target))
