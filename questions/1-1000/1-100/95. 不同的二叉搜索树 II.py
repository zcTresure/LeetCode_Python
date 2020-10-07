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

    def generateTrees(self, n: int) -> list:
        def generateTrees(start, end):
            if start > end:
                return [None, ]
            allTrees = []
            for i in range(start, end + 1):
                leftTrees = generateTrees(start, i - 1)
                rightTrees = generateTrees(i + 1, end)
                for l in leftTrees:
                    for r in rightTrees:
                        curTree = TreeNode(i)
                        curTree.left = l
                        curTree.right = r
                        allTrees.append(curTree)
            return allTrees
        return generateTrees(1, n) if n else []
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


num = 3
test = Solution()
roots = test.generateTrees(3)
for i in range(len(roots)):
    test.levelorderPrint(roots[i])
